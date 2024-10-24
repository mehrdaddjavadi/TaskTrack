{
    'name': 'Enhanced Project Management',
    'version': '1.0',
    'category': 'Project',
    'summary': 'Manage projects, tasks, and employee performance.',
    'description': """
        This module helps in managing projects, tasks, and employee performance.
        It includes features such as project creation, task assignment, and employee evaluation.
    """,
    'author': 'Mehrdad Javadi',
    'website': 'https://mehrdaddjavadi.github.io',
    'depends': ['base', 'hr'],
    'data': [
        'security/ir.model.access.csv',
        'views/project_view.xml',
        'views/task_view.xml',
        'views/employee_view.xml',
        'views/evaluation_view.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
