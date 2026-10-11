from django.contrib.admin.views.decorators import staff_member_required
from django.core.cache import cache
from django.shortcuts import redirect
from django.views.decorators.http import require_POST


@require_POST
@staff_member_required
def clear_cache(request):
    """Clear cached Django page content."""
    cache.clear()
    return redirect("page:home")
