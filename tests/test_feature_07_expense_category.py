from django.test import TestCase
from django.db import models


class FeatureTests(TestCase):
    def test_expense_category_model_exists(self):
        try:
            from receipts.models import ExpenseCategory  # noqa: F401
        except ModuleNotFoundError:
            self.fail("Could not find 'receipts.models.ExpenseCategory'")

    def test_expense_category_model_has_char_name_field(self):
        try:
            from receipts.models import ExpenseCategory

            name = ExpenseCategory.name
            self.assertIsInstance(
                name.field,
                models.CharField,
                msg="ExpenseCategory.name should be a character field",
            )
        except ModuleNotFoundError:
            self.fail("Could not find 'receipts.models'")
        except ImportError:
            self.fail("Could not find 'receipts.models.ExpenseCategory'")
        except AttributeError:
            self.fail("Could not find 'ExpenseCategory.name'")

    def test_expense_category_model_has_name_with_max_length_50_characters(
        self,
    ):
        try:
            from receipts.models import ExpenseCategory

            name = ExpenseCategory.name
            self.assertEqual(
                name.field.max_length,
                50,
                msg="The max length of ExpenseCategory.name should be 50",
            )
        except ModuleNotFoundError:
            self.fail("Could not find 'receipts.models'")
        except ImportError:
            self.fail("Could not find 'receipts.models.ExpenseCategory'")
        except AttributeError:
            self.fail("Could not find 'ExpenseCategory.name'")

    def test_expense_category_model_owner_has_many_to_one_relationship(
        self,
    ):
        try:
            from receipts.models import ExpenseCategory

            owner = ExpenseCategory.owner
            self.assertIsInstance(
                owner.field,
                models.ForeignKey,
                msg="ExpenseCategory should be a foreign key field",
            )
        except ModuleNotFoundError:
            self.fail("Could not find 'receipts.models'")
        except ImportError:
            self.fail("Could not find 'receipts.models.ExpenseCategory'")
        except AttributeError:
            self.fail("Could not find 'ExpenseCategory.owner'")

    def test_user_model_has_expense_category_related_name_of_categories(
        self,
    ):
        try:
            from receipts.models import ExpenseCategory

            owner = ExpenseCategory.owner
            self.assertEqual(
                owner.field.related_query_name(),
                "categories",
                msg="ExpenseCategory.owner should have a related name of 'categories'",
            )
        except ModuleNotFoundError:
            self.fail("Could not find 'receipts.models'")
        except ImportError:
            self.fail("Could not find 'receipts.models.ExpenseCategory'")
        except AttributeError:
            self.fail("Could not find 'ExpenseCategory.owner'")

    def test_expense_category_model_has_owner_related_to_auth_user(
        self,
    ):
        try:
            from receipts.models import ExpenseCategory
            from django.contrib.auth.models import User

            owner = ExpenseCategory.owner
            self.assertEqual(
                owner.field.related_model,
                User,
                msg="ExpenseCategory.owner should be related to the 'auth.User' model",  # noqa: E501
            )
        except ModuleNotFoundError:
            self.fail("Could not find 'receipts.models'")
        except ImportError:
            self.fail("Could not find 'receipts.models.ExpenseCategory'")
        except AttributeError:
            self.fail("Could not find 'ExpenseCategory.owner'")

    def test_expense_category_model_has_owner_has_on_delete_cascade(self):
        try:
            from receipts.models import ExpenseCategory

            owner = ExpenseCategory.owner
            self.assertEqual(
                owner.field.remote_field.on_delete,
                models.CASCADE,
                msg="ExpenseCategory should have CASCADE for on delete",
            )

        except ModuleNotFoundError:
            self.fail("Could not find 'receipts.models'")
        except ImportError:
            self.fail("Could not find 'receipts.models.ExpenseCategory'")
        except AttributeError:
            self.fail("Could not find 'ExpenseCategory.owner'")

    def test_expense_category_str_method_returns_name(self):
        try:
            from receipts.models import ExpenseCategory

            category = ExpenseCategory(name="My Category")
            self.assertEqual(
                str(category),
                "My Category",
                msg="ExpenseCategory.__str__ does not return the value of ExpenseCategory.name",
            )

        except ModuleNotFoundError:
            self.fail("Could not find 'tasks.models'")
        except ImportError:
            self.fail("Could not find 'tasks.models.Task'")
