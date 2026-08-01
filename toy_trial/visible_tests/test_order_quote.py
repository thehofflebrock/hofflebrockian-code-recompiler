import importlib.util
import os
from pathlib import Path
import unittest


def _load_target():
    configured = os.environ.get("ORDER_QUOTE_MODULE_PATH")
    if configured:
        target = Path(configured).expanduser().resolve()
    else:
        target = Path(__file__).resolve().parent.parent / "order_quote.py"

    if not target.is_file():
        raise RuntimeError(
            "Set ORDER_QUOTE_MODULE_PATH or place order_quote.py beside the tests directory"
        )

    spec = importlib.util.spec_from_file_location("hcr_order_quote_target", target)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.quote_order


quote_order = _load_target()


class VisibleOrderQuoteTests(unittest.TestCase):
    def test_us_standard(self):
        self.assertEqual(quote_order(1000, 1, "US"), 599)

    def test_us_free_threshold(self):
        self.assertEqual(quote_order(5000, 2, "US"), 0)

    def test_us_expedited(self):
        self.assertEqual(quote_order(1000, 1, "US", expedited=True), 1499)

    def test_us_free_promo(self):
        self.assertEqual(quote_order(2500, 1, "US", promo_code="FREESHIP"), 0)

    def test_half_shipping_rounds_down(self):
        self.assertEqual(quote_order(1000, 1, "US", promo_code="HALFSHIP"), 299)

    def test_member_discount(self):
        self.assertEqual(quote_order(1000, 1, "US", member=True), 399)

    def test_canada_standard(self):
        self.assertEqual(quote_order(8000, 1, "CA"), 1099)

    def test_canada_member_threshold(self):
        self.assertEqual(quote_order(7500, 1, "CA", member=True), 0)

    def test_international_standard(self):
        self.assertEqual(quote_order(1000, 1, "INTL"), 1799)

    def test_international_expedited_rejected(self):
        with self.assertRaisesRegex(ValueError, "expedited unavailable for INTL"):
            quote_order(1000, 1, "INTL", expedited=True)

    def test_bulk_fee_survives_free_shipping(self):
        self.assertEqual(quote_order(5000, 10, "US"), 250)


if __name__ == "__main__":
    unittest.main()

