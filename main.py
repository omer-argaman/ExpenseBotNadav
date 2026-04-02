"""
main.py — Test runner.

Simulates the bot in a terminal so every module can be tested without Telegram.
Type any expense message and it is parsed + logged to the sheet immediately.
Slash commands work exactly as they will in the real Telegram bot.

Usage:  python main.py   (run from inside the experiment/ folder)

Inputs:
  <expense>          — log to sheet   e.g. "groceries 120" or "250 fuel toyota"
  /help              — all commands
  /categories        — list categories
  /keywords <name>   — keywords for a category
  /summary           — monthly budget overview
  /category <name>   — details for one category
  /balance <name>    — remaining balance
  /delete            — show recent expenses and undo the most recent
  /delete <n>        — undo the nth most recent expense
  quit               — exit
"""

import logging
import re
logging.basicConfig(level=logging.WARNING)

import handlers.commands as commands
from handlers.message import process_expense
from parsing.parser import ParseResult


def _strip_html(text: str) -> str:
    """Remove HTML tags for clean terminal display."""
    return re.sub(r"<[^>]+>", "", text).replace("&lt;", "<").replace("&gt;", ">").replace("&amp;", "&")


def print_parse_result(result: ParseResult) -> None:
    print()
    print("─" * 55)
    print(f"  Input:    '{result.original_text}'")
    print(f"  Status:   {result.status}")
    print(f"  Category: {result.category}")
    print(f"  Amount:   {result.amount}")
    if result.suggestion:
        print(f"  Suggestion: '{result.suggestion}' ({result.suggestion_score}/100)")
    if result.error:
        print(f"  Info:     {result.error}")
    print("─" * 55)


def handle_command(raw: str) -> None:
    parts = raw.strip().split(maxsplit=1)
    cmd = parts[0].lower()
    arg = parts[1].strip() if len(parts) > 1 else ""

    if cmd == "/help":
        print(commands.help())

    elif cmd == "/categories":
        print(commands.categories())

    elif cmd == "/keywords":
        print(commands.keywords(arg) if arg else "Usage: /keywords <category name>")

    elif cmd == "/summary":
        print("Fetching from sheet...")
        text, _ = commands.summary()
        print(_strip_html(text))

    elif cmd == "/category":
        if not arg:
            print("Usage: /category <category name>")
        else:
            print("Fetching from sheet...")
            print(commands.category(arg))

    elif cmd == "/balance":
        if not arg:
            print("Usage: /balance <category name>")
        else:
            print(commands.balance(arg))

    elif cmd == "/delete":
        try:
            n = int(arg) if arg else 1
            print(commands.delete(n))
        except ValueError:
            print("Usage: /delete   or   /delete <number>  (e.g. /delete 3)")

    else:
        print(f"Unknown command: {cmd}. Type /help for available commands.")


def main():
    print()
    print("╔═════════════════════════════════════════════════════╗")
    print("║         Expense Bot — Test Runner                   ║")
    print("╠═════════════════════════════════════════════════════╣")
    print("║  <expense>    → parse and log to sheet              ║")
    print("║  /help        → all commands                        ║")
    print("║  quit         → exit                                ║")
    print("╚═════════════════════════════════════════════════════╝")

    while True:
        try:
            raw = input("\n> ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nExiting.")
            break

        if not raw:
            continue
        if raw.lower() in ("quit", "exit", "q"):
            print("Exiting.")
            break

        if raw.startswith("/"):
            handle_command(raw)
        else:
            reply, result = process_expense(raw)
            print_parse_result(result)
            print(f"\n  {reply}")


if __name__ == "__main__":
    main()
