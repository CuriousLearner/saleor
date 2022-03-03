#!/usr/bin/env python3
import os
import sys

if __name__ == "__main__":
    try:
        from decouple import RepositoryEnv
        file_path = os.path.normpath(os.path.join(os.path.dirname(__file__), "."))
        print("{}/.env".format(file_path))
        for k,v in RepositoryEnv("{}/.env".format(file_path)).data.items():
            # print(k, v)
            os.environ[k] = v
    except Exception as e:
        print(e)
        pass

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "saleor.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
