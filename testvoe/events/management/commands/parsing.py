import json
import os

from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = "The command simplifies loading data from JSON for Django ORM operation"

    def add_arguments(self, parser):
        parser.add_argument(
            "--new",
            "-n",
            type=str,
            required=True,
            help="Path to the new data file (output)",
        )
        parser.add_argument(
            "--old",
            "-o",
            type=str,
            required=True,
            help="Path to the old data file (input)",
        )

    def handle(self, *args, **options):
        new_file_path = options["new"]
        old_file_path = options["old"]

        if not os.path.exists(old_file_path):
            raise CommandError(f"Old file '{old_file_path}' does not exist.")

        if os.path.exists(new_file_path):
            raise CommandError(f"New file '{new_file_path}' already exists.")

        try:
            with open(old_file_path, "r", encoding="utf8") as old_file:
                content = []
                data = json.load(old_file)
                for obj in data:
                    info = {
                        "pk": obj["data"]["order"],
                        "model": "events.library",
                        "fields": {
                            "full_name": obj["data"]["full_name"],
                            "region": obj["data"]["region"],
                            "address": obj["data"]["address"],
                            "year": obj["data"]["year"],
                            "inter_budget_transfer_amount": obj["data"][
                                "inter_budget_transfer_amount"
                            ],
                        },
                    }
                    content.append(info)

            with open(new_file_path, "w", encoding="utf8") as new_file:
                json.dump(content, new_file, indent=4)

            self.stdout.write(
                self.style.SUCCESS(
                    f"Successfully simplifies content from '{old_file_path}' to '{new_file_path}'"
                )
            )

        except Exception as e:
            raise CommandError(f"An error occurred: {str(e)}")
