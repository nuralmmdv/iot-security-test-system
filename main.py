import argparse
from core.target import Target
from core.scanner import Scanner
from reports.json_report import JSONReport
from reports.html_report import HTMLReport


def parse_args():
    parser = argparse.ArgumentParser(
        description="IoT Security Test System - OWASP IoT Top 10 Scanner"
    )
    parser.add_argument(
        "-t", "--target",
        required=True,
        help="Target IP or hostname (e.g. 192.168.56.101)"
    )
    parser.add_argument(
        "-p", "--ports",
        nargs="+",
        type=int,
        help="Ports to scan (e.g. -p 22 80 443)"
    )
    parser.add_argument(
        "--timeout",
        type=int,
        default=5,
        help="Connection timeout in seconds (default: 5)"
    )
    parser.add_argument(
        "--report",
        choices=["json", "html", "both"],
        default="both",
        help="Report format (default: both)"
    )
    return parser.parse_args()


def main():
    args = parse_args()

    target = Target(
        host=args.target,
        ports=args.ports if args.ports else None,
        timeout=args.timeout
    )

    print("=" * 50)
    print("  IoT Security Test System")
    print("  OWASP IoT Top 10 Scanner")
    print("=" * 50)

    scanner = Scanner(target)
    findings = scanner.run()

    print("=" * 50)
    summary = scanner.summary()
    print(f"[*] Scan complete — {len(findings)} findings total")
    for severity, count in summary.items():
        print(f"    {severity:<10}: {count}")
    print("=" * 50)

    if findings:
        if args.report in ("json", "both"):
            JSONReport(findings, target).save()
        if args.report in ("html", "both"):
            HTMLReport(findings, target).save()


if __name__ == "__main__":
    main()
