
import argparse
from pathlib import Path
from .generator import load_csv_questions, export_txt
from .utils import select_questions

DEFAULT_N_TESTS = 10
DEFAULT_NO_REPEAT = True
DEFAULT_PDF = False


def build_tests(csv_dir: str, out_dir: str, n_tests: int, no_repeat: bool, pdf_enabled: bool):
    Path(out_dir).mkdir(parents=True, exist_ok=True)
    questions = load_csv_questions(csv_dir)
    for i in range(1, n_tests + 1):
        picked = select_questions(questions, n=25, no_repeat=no_repeat)
        export_txt(picked, str(Path(out_dir) / f"test_{i:02d}.txt"))
    if pdf_enabled:
        # Placeholder: futuro soporte PDF
        (Path(out_dir) / "_nota.txt").write_text("PDF activado, pendiente de implementación.", encoding='utf-8')


def main():
    parser = argparse.ArgumentParser(description="Generador de tests CCSE")
    parser.add_argument('--csv-dir', default='data/csv', help='Carpeta con CSV')
    parser.add_argument('--out-dir', default='build/tests', help='Salida de tests')
    parser.add_argument('--n-tests', type=int, default=DEFAULT_N_TESTS)
    parser.add_argument('--no-repeat', action='store_true', default=DEFAULT_NO_REPEAT)
    parser.add_argument('--pdf', dest='pdf', action='store_true', default=DEFAULT_PDF)
    parser.add_argument('--no-pdf', dest='pdf', action='store_false')
    args = parser.parse_args()

    build_tests(csv_dir=args.csv_dir, out_dir=args.out_dir, n_tests=args.n_tests, no_repeat=args.no_repeat, pdf_enabled=args.pdf)

if __name__ == '__main__':
    main()
