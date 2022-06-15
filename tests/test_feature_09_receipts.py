from django.test import TestCase
from django.db import models


class FeatureTests(TestCase):
    def test_receipt_model_exists(self):
        try:
            from receipts.models import Receipt  # noqa: F401
        except ModuleNotFoundError:
            self.fail("Could not find 'receipts.models.receipt'")

    def test_receipt_model_has_char_vendor_field(self):
        try:
            from receipts.models import Receipt

            vendor = Receipt.vendor
            self.assertIsInstance(
                vendor.field,
                models.CharField,
                msg="receipt.vendor should be a character field",
            )
        except ModuleNotFoundError:
            self.fail("Could not find 'receipts.models'")
        except ImportError:
            self.fail("Could not find 'receipts.models.receipt'")
        except AttributeError:
            self.fail("Could not find 'Receipt.vendor'")

    def test_receipt_model_has_vendor_with_max_length_200_characters(self):
        try:
            from receipts.models import Receipt

            vendor = Receipt.vendor
            self.assertEqual(
                vendor.field.max_length,
                200,
                msg="The max length of receipt.vendor should be 200",
            )
        except ModuleNotFoundError:
            self.fail("Could not find 'receipts.models'")
        except ImportError:
            self.fail("Could not find 'receipts.models.receipt'")
        except AttributeError:
            self.fail("Could not find 'Receipt.vendor'")

    def test_receipt_model_has_decimal_total_field(self):
        try:
            from receipts.models import Receipt

            total = Receipt.total
            self.assertIsInstance(
                total.field,
                models.DecimalField,
                msg="Receipt.total should be a decimal field",
            )
        except ModuleNotFoundError:
            self.fail("Could not find 'receipts.models'")
        except ImportError:
            self.fail("Could not find 'receipts.models.receipt'")
        except AttributeError:
            self.fail("Could not find 'Receipt.total'")

    def test_receipt_model_has_decimal_total_field_with_decimal_places_3(self):
        try:
            from receipts.models import Receipt

            total = Receipt.total
            self.assertEqual(
                total.field.decimal_places,
                3,
                msg="Receipt.total should have 3 decimal places",
            )
        except ModuleNotFoundError:
            self.fail("Could not find 'receipts.models'")
        except ImportError:
            self.fail("Could not find 'receipts.models.receipt'")
        except AttributeError:
            self.fail("Could not find 'Receipt.total'")

    def test_receipt_model_has_decimal_total_field_with_max_digits_10(self):
        try:
            from receipts.models import Receipt

            total = Receipt.total
            self.assertEqual(
                total.field.max_digits,
                10,
                msg="Receipt.total should have a max of 10 digits",
            )
        except ModuleNotFoundError:
            self.fail("Could not find 'receipts.models'")
        except ImportError:
            self.fail("Could not find 'receipts.models.receipt'")
        except AttributeError:
            self.fail("Could not find 'Receipt.total'")

    def test_receipt_model_has_decimal_tax_field(self):
        try:
            from receipts.models import Receipt

            tax = Receipt.tax
            self.assertIsInstance(
                tax.field,
                models.DecimalField,
                msg="Receipt.tax should be a decimal field",
            )
        except ModuleNotFoundError:
            self.fail("Could not find 'receipts.models'")
        except ImportError:
            self.fail("Could not find 'receipts.models.receipt'")
        except AttributeError:
            self.fail("Could not find 'Receipt.tax'")

    def test_receipt_model_has_decimal_tax_field_with_decimal_places_3(self):
        try:
            from receipts.models import Receipt

            tax = Receipt.tax
            self.assertEqual(
                tax.field.decimal_places,
                3,
                msg="Receipt.tax should have 3 decimal places",
            )
        except ModuleNotFoundError:
            self.fail("Could not find 'receipts.models'")
        except ImportError:
            self.fail("Could not find 'receipts.models.receipt'")
        except AttributeError:
            self.fail("Could not find 'Receipt.tax'")

    def test_receipt_model_has_decimal_tax_field_with_max_digits_10(self):
        try:
            from receipts.models import Receipt

            tax = Receipt.tax
            self.assertEqual(
                tax.field.max_digits,
                10,
                msg="Receipt.tax should have a max of 10 digits",
            )
        except ModuleNotFoundError:
            self.fail("Could not find 'receipts.models'")
        except ImportError:
            self.fail("Could not find 'receipts.models.receipt'")
        except AttributeError:
            self.fail("Could not find 'Receipt.tax'")

    def test_receipt_model_has_date_time_date_field(self):
        try:
            from receipts.models import Receipt

            date = Receipt.date
            self.assertIsInstance(
                date.field,
                models.DateTimeField,
                msg="Receipt.date should be a date time field",
            )
        except ModuleNotFoundError:
            self.fail("Could not find 'receipts.models'")
        except ImportError:
            self.fail("Could not find 'receipts.models.receipt'")
        except AttributeError:
            self.fail("Could not find 'Receipt.date'")
