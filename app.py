from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import datetime
import json
import os

app = Flask(__name__)
app.secret_key = 'tu_clave_secreta_aqui'

# Archivo para almacenar las tareas
TASKS_FILE = 'tasks.json'

def load_tasks():
    """Cargar tareas desde el archivo JSON"""
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    """Guardar tareas en el archivo JSON"""
    with open(TASKS_FILE, 'w', encoding='utf-8') as f:
        json.dump(tasks, f, ensure_ascii=False, indent=2)

@app.route('/')
def index():
    """Página principal que muestra todas las tareas"""
    tasks = load_tasks()
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    """Agregar una nueva tarea"""
    task_text = request.form.get('task_text', '').strip()
    
    if not task_text:
        flash('La tarea no puede estar vacía', 'error')
        return redirect(url_for('index'))
    
    tasks = load_tasks()
    new_task = {
        'id': len(tasks) + 1,
        'text': task_text,
        'completed': False,
        'created_at': datetime.now().isoformat()
    }
    
    tasks.append(new_task)
    save_tasks(tasks)
    flash('Tarea agregada exitosamente', 'success')
    
    return redirect(url_for('index'))

@app.route('/complete/<int:task_id>')
def complete_task(task_id):
    """Marcar una tarea como completada"""
    tasks = load_tasks()
    
    for task in tasks:
        if task['id'] == task_id:
            task['completed'] = True
            task['completed_at'] = datetime.now().isoformat()
            break
    
    save_tasks(tasks)
    flash('Tarea marcada como completada', 'success')
    
    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    """Eliminar una tarea"""
    tasks = load_tasks()
    tasks = [task for task in tasks if task['id'] != task_id]
    save_tasks(tasks)
    flash('Tarea eliminada', 'info')
    
    return redirect(url_for('index'))

@app.route('/toggle/<int:task_id>')
def toggle_task(task_id):
    """Alternar el estado de una tarea (completada/pendiente)"""
    tasks = load_tasks()
    
    for task in tasks:
        if task['id'] == task_id:
            task['completed'] = not task['completed']
            if task['completed']:
                task['completed_at'] = datetime.now().isoformat()
            else:
                task.pop('completed_at', None)
            break
    
    save_tasks(tasks)
    return redirect(url_for('index'))

@app.route('/edit/<int:task_id>')
def edit_task_form(task_id):
    """Mostrar formulario de edición de tarea"""
    tasks = load_tasks()
    task = None
    
    for t in tasks:
        if t['id'] == task_id:
            task = t
            break
    
    if not task:
        flash('Tarea no encontrada', 'error')
        return redirect(url_for('index'))
    
    return render_template('edit.html', task=task)

@app.route('/update/<int:task_id>', methods=['POST'])
def update_task(task_id):
    """Actualizar el texto de una tarea"""
    new_text = request.form.get('task_text', '').strip()
    
    if not new_text:
        flash('La tarea no puede estar vacía', 'error')
        return redirect(url_for('edit_task_form', task_id=task_id))
    
    tasks = load_tasks()
    
    for task in tasks:
        if task['id'] == task_id:
            task['text'] = new_text
            task['updated_at'] = datetime.now().isoformat()
            break
    
    save_tasks(tasks)
    flash('Tarea actualizada exitosamente', 'success')
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
