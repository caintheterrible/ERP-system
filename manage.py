import os,sys

def main():

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app_config.settings.development')

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            'Could not import Django. Ensure it is installed and available on your Python PATH.'
        ) from exc


    execute_from_command_line(sys.argv)

if __name__=='__main__':
    main()