from django.shortcuts import redirect


def editors_permissions():
    def decorator(account_func):
        def wrapper_account(request, *args, **kwargs):
            if request.user.groups.exists():
                group_list = []
                for groups in request.user.groups.all():
                    group_list.append(str(groups).lower())

                if 'coaches' not in group_list:
                    return redirect('account_inform')
            else:
                return redirect('account_inform')
            return account_func(request, *args, **kwargs)
        return wrapper_account
    return decorator
