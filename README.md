# pg_migrator_checker

Script for checking if migration process where ok in big amount of data.
It just checks if the number of rows in the source table is the same as in the destination table.

## Usage

1. Create a copy of .env.example and configure it with your db credentials and dbs names.
    
```bash
cp .env.example .env
```

2. Create a virtual environment and install the requirements.

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
3. Run the script

```bash
python3 -m data_checker
```
