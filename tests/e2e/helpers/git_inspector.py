"""
tests/e2e/helpers/git_inspector.py
Inspection utilities for Git repository status, remote tracking, and filesystem audits.
"""
import os
from pathlib import Path
import shutil
import subprocess
from typing import Any, Dict, List, Optional, Tuple

TupleResult = Tuple[int, str, str]

def _run_git(args: List[str], cwd: Optional[Path] = None) -> TupleResult:
    """Executes a git command safely."""
    git_bin = shutil.which("git") or "git"
    try:
        proc = subprocess.run(
            [git_bin] + args,
            cwd=str(cwd) if cwd else None,
            capture_output=True,
            text=True,
            shell=False,
            check=False
        )
        return proc.returncode, proc.stdout.strip(), proc.stderr.strip()
    except Exception as e:
        return 1, "", str(e)

def get_git_branch(cwd: Optional[Path] = None) -> str:
    """Returns the name of the currently checked out branch."""
    code, out, _ = _run_git(["rev-parse", "--abbrev-ref", "HEAD"], cwd)
    return out if code == 0 else ""

def get_git_remote_url(remote_name: str = "origin", cwd: Optional[Path] = None) -> str:
    """Returns the remote URL for the specified remote name."""
    code, out, _ = _run_git(["remote", "get-url", remote_name], cwd)
    return out if code == 0 else ""

def get_git_commit_hash(ref: str = "HEAD", cwd: Optional[Path] = None) -> str:
    """Returns the commit hash for the given reference."""
    code, out, _ = _run_git(["rev-parse", ref], cwd)
    return out if code == 0 else ""

def get_git_status_porcelain(cwd: Optional[Path] = None, exclude_meta: bool = True) -> List[str]:
    """
    Returns modified/untracked files from git status --porcelain.
    Excludes .agents/ and tests/ by default to focus on production work products.
    """
    code, out, _ = _run_git(["status", "--porcelain"], cwd)
    if code != 0 or not out:
        return []

    lines = [line.strip() for line in out.splitlines() if line.strip()]
    if exclude_meta:
        filtered = []
        for line in lines:
            parts = line.split(maxsplit=1)
            if len(parts) == 2:
                path_part = parts[1].replace('"', '')
                if path_part.startswith(".agents") or path_part.startswith("tests"):
                    continue
            filtered.append(line)
        return filtered
    return lines

def get_git_latest_commit_info(cwd: Optional[Path] = None) -> str:
    """Returns the author, email, and subject of the HEAD commit."""
    code, out, _ = _run_git(["log", "-1", "--pretty=format:%an <%ae> - %s"], cwd)
    return out if code == 0 else ""

def audit_whitelist_assets(root_path: Path | str, whitelist: List[str]) -> Dict[str, Any]:
    """Verifies that all whitelisted static assets exist and have size > 0."""
    root = Path(root_path)
    missing = []
    zero_byte = []
    valid = []

    for rel_path in whitelist:
        full_path = root / rel_path
        if not full_path.exists():
            missing.append(rel_path)
        elif full_path.stat().st_size == 0:
            zero_byte.append(rel_path)
        else:
            valid.append(rel_path)

    return {
        "total": len(whitelist),
        "valid_count": len(valid),
        "missing": missing,
        "zero_byte": zero_byte,
        "all_valid": len(missing) == 0 and len(zero_byte) == 0
    }

def audit_unreferenced_in_source(root_path: Path | str, target_dir_name: str) -> bool:
    """
    Verifies that target_dir_name (e.g. 'assets/') is not referenced by any import
    or asset load in src/ or index.html.
    """
    root = Path(root_path)
    src_dir = root / "src"
    index_file = root / "index.html"

    # Search for relative paths starting with target_dir_name, e.g. "./assets/" or "assets/"
    import re
    # We want to check if src code references root 'assets/' directly as a relative import
    # like from '../assets/...' or import from 'assets/...'
    pattern = re.compile(rf'["\'](?:\.\./)*{target_dir_name}/', re.IGNORECASE)

    for path in list(src_dir.rglob("*.jsx")) + list(src_dir.rglob("*.js")) + [index_file]:
        if path.exists():
            text = path.read_text(encoding="utf-8", errors="ignore")
            # If it's an import statement referencing root assets
            for line in text.splitlines():
                if "import " in line and pattern.search(line):
                    return False
    return True
