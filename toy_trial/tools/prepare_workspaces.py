"""Create matched blind and control workspaces for the HCR v0.1 toy trial."""

from __future__ import annotations

import argparse
from pathlib import Path
import shutil


TOY_ROOT = Path(__file__).resolve().parents[1]
PACKAGE_ROOT = TOY_ROOT.parent


def resolved_file(value: str) -> Path:
    path = Path(value).expanduser()
    if not path.is_absolute():
        path = (Path.cwd() / path).resolve()
    else:
        path = path.resolve()
    if not path.is_file():
        raise argparse.ArgumentTypeError(f"not a file: {path}")
    return path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--packet", required=True, type=resolved_file)
    parser.add_argument("--handoff", type=resolved_file)
    parser.add_argument("--output", type=Path, default=TOY_ROOT / "runs")
    args = parser.parse_args()

    output = args.output.expanduser()
    if not output.is_absolute():
        output = (Path.cwd() / output).resolve()
    else:
        output = output.resolve()

    if output.exists():
        raise SystemExit(
            f"refusing to overwrite existing run directory: {output}\n"
            "Move or archive it, then run the preparation command again."
        )

    control = output / "control"
    blind = output / "blind"
    for workspace in (control, blind):
        (workspace / "tests").mkdir(parents=True)
        shutil.copy2(args.packet, workspace / "RECONSTRUCTION_PACKET.md")
        if args.handoff:
            shutil.copy2(args.handoff, workspace / "ARCHITECT_HANDOFF.md")
        shutil.copy2(PACKAGE_ROOT / "templates" / "06_BUILD_RECORD.md", workspace / "BUILD_RECORD.md")
        shutil.copy2(
            TOY_ROOT / "visible_tests" / "test_order_quote.py",
            workspace / "tests" / "test_order_quote.py",
        )

    shutil.copy2(TOY_ROOT / "legacy" / "order_quote.py", control / "order_quote.py")
    shutil.copy2(TOY_ROOT / "builder_stub" / "order_quote.py", blind / "order_quote.py")

    (control / "WORKSPACE_README.md").write_text(
        "# Control workspace\n\n"
        "Use the package prompt `prompts/07_CONTROL_REFACTOR.md`. The inherited "
        "implementation is intentionally present. Do not navigate to the blind or "
        "auditor workspaces.\n",
        encoding="utf-8",
    )
    (blind / "WORKSPACE_README.md").write_text(
        "# Blind workspace\n\n"
        "Use the package prompt `prompts/05_BUILDER.md`. Do not navigate to parent "
        "or sibling directories. The legacy implementation, repository history, audit "
        "set, evaluator, and control candidate are forbidden.\n",
        encoding="utf-8",
    )

    print(f"created control workspace: {control}")
    print(f"created blind workspace: {blind}")
    print("Open each directory as a separate workspace in a separate fresh session.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

