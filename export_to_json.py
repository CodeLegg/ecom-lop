import os
import django
import json
from decimal import Decimal
from datetime import datetime, timedelta
from django.apps import apps

# Custom JSON encoder to handle Decimal, datetime, and timedelta objects
class CustomJSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, Decimal):
            return float(o)
        elif isinstance(o, datetime):
            return o.isoformat()
        elif isinstance(o, timedelta):
            return str(o)
        return super().default(o)

def export_model_data_to_json(output_file):
    try:
        data = {}
        for model in apps.get_models():
            model_name = model._meta.model_name
            model_data = list(model.objects.all().values())
            data[model_name] = model_data

        with open(output_file, 'w') as f:
            json.dump(data, f, indent=4, cls=CustomJSONEncoder)  # Use the custom encoder

        print("Data exported to", output_file)
    except Exception as e:
        print("Error exporting data:", e)

try:
    # Set up Django
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ecom.settings")
    django.setup()

    # Set the name of the output JSON file
    OUTPUT_FILE = "data.json"

    # Export data to JSON
    export_model_data_to_json(OUTPUT_FILE)
except Exception as e:
    print("Error:", e)
