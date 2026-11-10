#!/usr/bin/env bash
# Optional local GitHub auth/repository discovery. Source from a trusted location.
# No credential-file scraping, secret output or global config change.
# gh auth status may contact the configured host to check authentication.
# GH_USER is intentionally unresolved; look up account identity only when needed.

GH_AUTH_METHOD="none"
GH_USER=""
GH_OWNER=""
GH_REPO=""
GH_OWNER_REPO=""
if command -v gh >/dev/null 2>&1 && gh auth status >/dev/null 2>&1; then
    GH_AUTH_METHOD="gh"
elif [ -n "${GITHUB_TOKEN:-}" ] || [ -n "${GH_TOKEN:-}" ]; then
    GH_AUTH_METHOD="curl"
fi

_task_github_remote=$(git remote get-url origin 2>/dev/null) || _task_github_remote=""
_task_github_repo=""
case "$_task_github_remote" in
    https://github.com/*) _task_github_repo=${_task_github_remote#https://github.com/} ;;
    git@github.com:*) _task_github_repo=${_task_github_remote#git@github.com:} ;;
    ssh://git@github.com/*) _task_github_repo=${_task_github_remote#ssh://git@github.com/} ;;
esac
_task_github_repo=${_task_github_repo%/}
_task_github_repo=${_task_github_repo%.git}
if [[ $_task_github_repo =~ ^[[:alnum:]_.-]+/[[:alnum:]_.-]+$ ]]; then
    GH_OWNER_REPO=$_task_github_repo
    GH_OWNER=${GH_OWNER_REPO%/*}
    GH_REPO=${GH_OWNER_REPO#*/}
fi
unset _task_github_remote _task_github_repo
export GH_AUTH_METHOD GH_USER GH_OWNER GH_REPO GH_OWNER_REPO
