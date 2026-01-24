## HOW DID I MAKE THIS PROJECT?
1. Create the project folder and its contents
- I'll skip through the project folder creation process, first I made the "skeleton" structure for this project by using bash commands such as mkdir, cd, touch, pwd, etc...
- When done creating the project structure, I navigated to the root folder "basic-flask-app".
# Install Python (and pip) if not installed already
- I ran -> sudo apt install python3
- Then I ran -> sudo apt install python3-pip
2. Create and activate a virtual environment
- I ran -> sudo apt install python3-venv
- In bash execute -> python3 -m venv venv
- Then I activated the venv -> source venv/bin/activate
- After that, I installed Flask in the venv -> pip install flask
- And I echoed the required Python packages into the requirements.txt file -> pip freeze > requirements.txt
3. Create Flask app of your choice, and run it
- I went with the simplest possible Flask app
- In app.py, I built my Flask app and ran it -> python app.py
- The bash outputs "Running on: [domain]", I copied that domain and ran it in my browser.
4. Add HTML templates
# As I had mentioned, I already created the whole file structure, because I am following a walkthrough for this project. But at this moment, we would run -> mkdir templates, and in the templates dir, we would create an index.html file.
- I created a basic HTML page.
- I edited app.py to return render_template that starts the HTML page.
- I refreshed the app to see the new output.
5. Add static files
- In the static directory, I made a basic .css and .js file.
- I updated templates/index.html to load both the .css style and the .js script.
- After that, I refreshed the app.
6. Add a second page + template inheritance
- In templates/base.html, I made a base HTML page containing:
    - Block in <head> for the title
    - Style and script refs
    - A navigation bar with two hrefs to "/" (Home) and "/about" (About)
    - Block in <body> for the content
- I updated index.html to use the base layout
- I created a basic About page in templates/about.html
- I added the /about route in app.py
- I refreshed the app.
7. Convert app to use blueprints
# Blueprints let you split your app into logical parts. Right now everything is inside app.py. We’re going to move the routes into a separate folder.
- In blueprints/main.py, I created the main blueprint.
- Afterwards, I updated app.py to use the blueprint. I created something called the "app factory pattern".
- I refreshed the app.
# Now, we have achieved a modular Flask app. This design approach allows us to create multiple application instances with different configs. This is useful for real Flask app production.
8. Add an API blueprint
# This will give the app a clean separation between web pages and API endpoints. This is a structure that is able to scale when you want to add more features later.
- First I created a basic API blueprint with one GET endpoint in blueprints/api.py
- Then, I updated app.py to register the API blueprint. The result of this is that all routes inside api_bp will start with /api.
- I refreshed the app, and tested the result in [domain]/api/status, which i defined in my api.py file.
9. Add config
- Inside config.py, I created a simple config class containing a secret key.
- I updated app.py to load the config file.
- I refreshed the app.
# The app hasn't changed much, but internally, the Flask app now has a secret key, and a scalable structure. This resembles how real Flask app foundations are built.
10. Build a proper homepage layout
# This layout is going to contain a hero section, an "About me" preview, a "Favorite programming languages" section and a footer.
- In index.html, I replaced the plain <h1> title with a <p> paragraph to a more structured version, just to resemble a proper web page.
- I also updated the static/style.css file to style my new page structure.
- I refreshed the app.
11. Add a "Favorite programming languages" system (data -> template)
- I modified main.py to contain a list of objects, that contain basic info about my favorite programming languages. Afterwards, I passed that list into the index template.
- In templates/index.html, i used a Jinja2 for loop to display the language list.
- In static/style.css, I added styles for the language cards.
- I refreshed the app.
12. Add a languages page, and a dedicated page for each language
- I updated the languages list by adding "id" and "experience" values, aswell as their specific link to a detailed info page.
- In templates/languages.html, I added a page structure for viewing the languages for loop, similar to the one I've created in step 11.
- In blueprints/main.py, I've added a route for the languages template.
- In blueprints/detail.html, I made a basic page structure to view the details of a specific language.
- In main.py, I've added a dynamic route to view the detail page for the selected language.
- I refreshed my app.
13. Add nav link to languages + layout and footer updates
- To the navigation bar in templates/base.html, I added a href to the languages subdomain. I also added a footer to the HTML document.
- In static/style.css, I added the styles for these new elements.
- I refreshed the app.