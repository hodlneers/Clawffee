"""Command line entrypoint for Clawffee."""

from __future__ import annotations

import argparse
import sys

from .reporting import to_json, to_markdown
from .security_inspector import SecurityInspector


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Clawffee security inspector")
    parser.add_argument("target", help="File or directory to inspect")
    parser.add_argument(
        "--format",
        choices=["json", "md"],
        default="json",
        help="Output format",
    )
    return parser


def main() -> int:
    parser = _build_parser()
    args = parser.parse_args()

    inspector = SecurityInspector()
    report = inspector.inspect(args.target)

    if args.format == "md":
        print(to_markdown(report))
    else:
        print(to_json(report))

    return 0


if __name__ == "__main__":
    sys.exit(main())
