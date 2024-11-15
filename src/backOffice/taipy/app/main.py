from taipy.gui import Gui
import pandas as pd

light_theme = {
    "palette": {
        "background": {
            "default": "#d580ff"  
        },
        "primary": {"main": "#ffffff"}
    }
}

dark_theme = {
    "palette": {
        "background": {
            "default": "#111111"  
        },
        "primary": {"main": "#eeeeee"}
    }
}

site_logo_url = "https://example.com/logo.png"  # Replace with your logo URL
site_name = "My Site Name"


root = """

<|Talent Map|navbar|> 
<|content|>
_This is a footer_
"""

# Define the content for different pages
home_page = """
# Home

Dashboard goes here
"""

clients_page = """
# Clients

Welcome to the clients page!
"""

jobs_page = """
# Jobs

<|{df}|table|pagination=5|filter=true|sortable=true|draggable|orient=horizontal|>
"""

candidates_page = """
# Candidates

Candidates goes here
"""

data_file = "D:/wspc3/github/TalentMap/data/sample/resumes.csv"
df = pd.read_csv(data_file)
print(df.head())

pages = {
    "/": root,
    "home":  home_page,
    "clients": clients_page,
    "jobs":  jobs_page,
    "candidates":  candidates_page
}

if __name__ == "__main__":
    # gui = Gui(pages={**pages, "navbar": navbar})
    gui = Gui(pages={**pages})
    gui.run(title="Talent Map", use_reloader=True, port=3636, light_theme=light_theme, dark_theme=dark_theme)