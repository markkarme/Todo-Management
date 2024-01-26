# -*- coding: utf-8 -*-
# from odoo import http


# class TodoManagment(http.Controller):
#     @http.route('/todo_managment/todo_managment', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/todo_managment/todo_managment/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('todo_managment.listing', {
#             'root': '/todo_managment/todo_managment',
#             'objects': http.request.env['todo_managment.todo_managment'].search([]),
#         })

#     @http.route('/todo_managment/todo_managment/objects/<model("todo_managment.todo_managment"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('todo_managment.object', {
#             'object': obj
#         })
