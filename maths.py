admins = {"Dedan","Chakin"}
editors ={"Chakin","aaron"}

#combine both groups
all_users = admins.union(editors)
print("all users", all_users)

#who's both admin and editor?

both_roles = admins.intersection(editors)
print("users with both roles", both_roles)

admin_only = admins.difference(editors)
print("users with admin role only", admin_only)