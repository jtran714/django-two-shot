from django.test import TestCase
from django.db import models


class FeatureTests(TestCase):
    def test_account_model_exists(self):
        try:
            from receipts.models import Account  # noqa: F401
        except ModuleNotFoundError:
            self.fail("Could not find 'receipts.models.Account'")

    def test_account_model_has_char_name_field(self):
        try:
            from receipts.models import Account

            name = Account.name
            self.assertIsInstance(
                name.field,
                models.CharField,
                msg="receipt.name should be a character field",
            )
        except ModuleNotFoundError:
            self.fail("Could not find 'receipts.models'")
        except ImportError:
            self.fail("Could not find 'receipts.models.Account'")
        except AttributeError:
            self.fail("Could not find 'Account.name'")

    def test_account_model_has_name_with_max_length_100_characters(
        self,
    ):
        try:
            from receipts.models import Account

            name = Account.name
            self.assertEqual(
                name.field.max_length,
                100,
                msg="The max length of receipt.name should be 100",
            )
        except ModuleNotFoundError:
            self.fail("Could not find 'receipts.models'")
        except ImportError:
            self.fail("Could not find 'receipts.models.Account'")
        except AttributeError:
            self.fail("Could not find 'Account.name'")

    def test_account_model_has_char_number_field(self):
        try:
            from receipts.models import Account

            name = Account.name
            self.assertIsInstance(
                name.field,
                models.CharField,
                msg="Account.number should be a character field",
            )
        except ModuleNotFoundError:
            self.fail("Could not find 'receipts.models'")
        except ImportError:
            self.fail("Could not find 'receipts.models.Account'")
        except AttributeError:
            self.fail("Could not find 'Account.name'")

    def test_account_model_has_number_with_max_length_20_characters(
        self,
    ):
        try:
            from receipts.models import Account

            number = Account.number
            self.assertEqual(
                number.field.max_length,
                20,
                msg="The max length of Account.number should be 20",
            )
        except ModuleNotFoundError:
            self.fail("Could not find 'receipts.models'")
        except ImportError:
            self.fail("Could not find 'receipts.models.Account'")
        except AttributeError:
            self.fail("Could not find 'Account.name'")

    def test_account_model_owner_has_many_to_one_relationship(
        self,
    ):
        try:
            from receipts.models import Account

            owner = Account.owner
            self.assertIsInstance(
                owner.field,
                models.ForeignKey,
                msg="Account should be a foreign key field",
            )
        except ModuleNotFoundError:
            self.fail("Could not find 'receipts.models'")
        except ImportError:
            self.fail("Could not find 'receipts.models.Account'")
        except AttributeError:
            self.fail("Could not find 'Account.owner'")

    def test_user_model_has_account_related_name_of_categories(
        self,
    ):
        try:
            from receipts.models import Account

            owner = Account.owner
            self.assertEqual(
                owner.field.related_query_name(),
                "accounts",
                msg="Account.owner should have a related name of 'accounts'",
            )
        except ModuleNotFoundError:
            self.fail("Could not find 'receipts.models'")
        except ImportError:
            self.fail("Could not find 'receipts.models.Account'")
        except AttributeError:
            self.fail("Could not find 'Account.owner'")

    def test_account_model_has_owner_related_to_auth_user(
        self,
    ):
        try:
            from receipts.models import Account
            from django.contrib.auth.models import User

            owner = Account.owner
            self.assertEqual(
                owner.field.related_model,
                User,
                msg="Account.owner should be related to the 'auth.User' model",  # noqa: E501
            )
        except ModuleNotFoundError:
            self.fail("Could not find 'receipts.models'")
        except ImportError:
            self.fail("Could not find 'receipts.models.Account'")
        except AttributeError:
            self.fail("Could not find 'Account.owner'")

    def test_account_model_has_owner_has_on_delete_cascade(self):
        try:
            from receipts.models import Account

            owner = Account.owner
            self.assertEqual(
                owner.field.remote_field.on_delete,
                models.CASCADE,
                msg="Account should have CASCADE for on delete",
            )

        except ModuleNotFoundError:
            self.fail("Could not find 'receipts.models'")
        except ImportError:
            self.fail("Could not find 'receipts.models.Account'")
        except AttributeError:
            self.fail("Could not find 'Account.owner'")

    def test_account_str_method_returns_name(self):
        try:
            from receipts.models import Account

            category = Account(name="My Category")
            self.assertEqual(
                str(category),
                "My Category",
                msg="Account.__str__ does not return the value of Account.name",
            )

        except ModuleNotFoundError:
            self.fail("Could not find 'tasks.models'")
        except ImportError:
            self.fail("Could not find 'tasks.models.Task'")
