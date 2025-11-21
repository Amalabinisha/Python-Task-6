# Python-Task-6

## Portfolio Website (Flask)

### Overview
This is a simple portfolio website built using Flask. It includes a home page and a contact page. The website uses Jinja2 templates and basic styling with CSS.

### Features
- Flask routing for home (`/`) and contact (`/contact`) pages
- Contact form using GET/POST methods
- Dynamic messages using Jinja2
- Organized folder structure with templates and static files

### Folder Structure
```
portfolio_flask/
├── app.py
├── templates/
│   ├── index.html
│   └── contact.html
└── static/
    └── style.css
```

### How to Run
1. Install Flask:
   ```
   pip install flask
   ```
2. Save all project files in the folder structure shown above.
3. Run the Flask application:
   ```
   python app.py
   ```
4. Open your browser and go to:
   ```
   http://127.0.0.1:5000/
   ```

### Technologies Used
- Python 3.x  
- Flask  
- HTML (Jinja2 Templates)  
- CSS  

### Notes
- You can edit `index.html` and `contact.html` to add your own portfolio details.
- The contact form does not send data externally; it only displays a success message on submission.

### Output Screenshot

<img width="470" height="313" alt="Screenshot 2025-11-21 200713" src="https://github.com/user-attachments/assets/7e59b0a8-1cce-4224-9b5b-9a6d178294e4" />

<img width="334" height="392" alt="Screenshot 2025-11-21 200735" src="https://github.com/user-attachments/assets/2908cbc6-c7cd-4bd0-b065-33edc32dc2b2" />
