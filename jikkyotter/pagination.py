from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def paginate_query(self, queryset, count):
    paginator = Paginator(queryset, count)
    page = self.request.GET.get('page')
    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)
    return page_obj
