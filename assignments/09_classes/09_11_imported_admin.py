from privileges import admin

admin_1 = Admin('Adam', 'Admin', 'NYC', 26, ['can add post', 'can delete post', 'can ban user'])
admin_1.privileges.show_privileges()