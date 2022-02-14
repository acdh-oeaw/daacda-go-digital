[![DOI](https://zenodo.org/badge/132461159.svg)](https://zenodo.org/badge/latestdoi/132461159)

# DAACDA
Downed Allied Air Crew Database Austria. A web application.

## About
The repository of the web application Downed Allied Air Crew Database Austria. The application’s purpose is the publication of data about Allied air crews whose planes were downed above Austria during World War II. The data running this application was gathered by Georg Hoffmann and Nicole Goll. For more information please refer to [Hoffmann, Fliegerlynchjustiz, 2015](https://www.schoeningh.de/katalog/titel/978-3-506-78137-6.html) or [Goll/Hoffmann, Missing in Action, 2016](http://www.bundesheer.at/download_archiv/pdfs/missing_in_action.pdf).


## Install
1. Clone this repository.
2. Create and activate a virtual environment.
3. Install the required packages `pip install -r requirements.txt`.
4. Run `makemigrations`, `migrate` and `runserver`.
5. Open [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

This project uses modularized settings (to keep sensitive information out of version control or to be able to use the same code for development and production). Therefore you'll have to append a `--settings` parameter pointing to the settings file you'd like to run the code with to all `manage.py` commands. For example, run `python manage.py makemigrations --settings=daacda.settings.dev`.

## Upload Data
To import data, you have to execute the ipython script `import_data.ipynb`.

1. Start a new ipython session `python manage.py shell_plus --notebook --settings=daacda.settings.dev_custom`.
2. Execute the script cell by cell.



### building the image

`docker build -t daacda:latest .`
`docker build -t daacda:latest --no-cache .`

### running the image

To run the image you should provide an `env.default` file to pass in needed environment variables; see example `env.default` in this repo:


`docker run -it -p 8020:8020 --rm --env-file env.default daacda:latest`

### or use published image:

`docker run -it -p 8020:8020 --rm --env-file env.default acdhch/daacda:latest`