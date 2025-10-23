from django.core.management import call_command
from django.core.management.base import BaseCommand
from termcolor import colored

from apps.users_app.models.groups import Groups
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = "Loads initial fixtures"

    call_command("loaddata", "auth.group.json")
    print(
        colored(
            "Successfully added group permissions",
            "green",
            attrs=["blink"],
        )
    )

    admin_user = User.objects.get(username="admin")
    admin_user.groups.add(Groups.SUPER_ADMIN)
    print(
        colored(
            "Promoted default admin user as SUPER_ADMIN",
            "blue",
            attrs=["blink"],
        )
    )

    call_command("loaddata", "area_type.json")
    print(
        colored(
            "Successfully added area_type information",
            "green",
            attrs=["blink"],
        )
    )
    call_command("loaddata", "area.json")
    print(
        colored(
            "Successfully added area information",
            "green",
            attrs=["blink"],
        )
    )
    call_command("loaddata", "area_nodes.json")
    print(
        colored(
            "Successfully added area_nodes information",
            "green",
            attrs=["blink"],
        )
    )
    call_command("loaddata", "pluviometer_type.json")
    print(
        colored(
            "Successfully added pluviometer_type information",
            "green",
            attrs=["blink"],
        )
    )
    call_command("loaddata", "pluviometer.json")
    print(
        colored(
            "Successfully added pluviometer information",
            "green",
            attrs=["blink"],
        )
    )
    call_command("loaddata", "diary_precipitation_classification.json")
    print(
        colored(
            "Successfully added diary precipitation classification information",
            "green",
            attrs=["blink"],
        )
    )
    call_command("loaddata", "year_statistics.json")
    print(
        colored(
            "Successfully added year statistics information",
            "green",
            attrs=["blink"],
        )
    )

    call_command("loaddata", "month_statistics.json")
    print(
        colored(
            "Successfully added month statistics information",
            "green",
            attrs=["blink"],
        )
    )

    call_command("loaddata", "registers.json")
    print(
        colored(
            "Successfully added registers information",
            "green",
            attrs=["blink"],
        )
    )
    call_command("loaddata", "pluviometer_area.json")
    print(
        colored(
            "Successfully added pluviometer_area information",
            "green",
            attrs=["blink"],
        )
    )

    call_command("loaddata", "precipitation_concentration_index_by_area.json")
    print(
        colored(
            "Successfully added precipitation concentration index by area information",
            "green",
            attrs=["blink"],
        )
    )

    call_command("loaddata", "precipitation_concentration_index_by_pluvimeter.json")
    print(
        colored(
            "Successfully added precipitation concentration index by pluviometer information",
            "green",
            attrs=["blink"],
        )
    )

    call_command("loaddata", "precipitation_concentration_index_monthly_by_area.json")
    print(
        colored(
            "Successfully added precipitation concentration index monthly by area information",
            "green",
            attrs=["blink"],
        )
    )

    call_command(
        "loaddata", "precipitation_concentration_index_monthly_by_pluviometer.json"
    )
    print(
        colored(
            "Successfully added precipitation concentration index monthly by pluviometer information",
            "green",
            attrs=["blink"],
        )
    )
