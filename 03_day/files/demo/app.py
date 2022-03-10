#app.py

from user_pkg.user import User
from user_pkg.admin_user import AdminUser


jim = User("jim", "jim@dm.com")
michael = AdminUser("michael", "ms@dm.com")