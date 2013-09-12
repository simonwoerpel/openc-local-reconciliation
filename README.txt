A skeleton for creating an OpenRefine reconciliation service.

This repository is intended to be a basic template for a Refine reconciliation service.  It is expected that you would modify the included code for your own purposes.

Requirements:
1. Python
2. virtualenv

Instructions:

1. Download the files in this repository to a directory on your computer. 

     $ git clone git://github.com/OpenRefine/reconciliation_service_skeleton.git my_recon_service
     $ cd my_recon_service
     
2. Create a new virtual environment
     $ virtualenv venv
     
3. Activate the newly created virtual environment

     $ venv/bin/activate

   or on Windows

     $ venv\scripts\activate

4. Install the dependencies

     $ pip install Flask simplejson fuzzywuzzy
     
5. Run 'example_composers_reconciliation_service.py' e.g. 

     $ cd my_recon_service
     $ python example_composers_reconciliation_service.py'.

   This will start a reconciliation service on port 5000 which you can use with Refine by using the URL http://127.0.0.1:5000/reoncile
