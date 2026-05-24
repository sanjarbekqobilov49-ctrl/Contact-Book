from django.contrib import messages
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Count
from django.shortcuts import get_object_or_404, redirect, render

from .filters import ContactFilter
from .forms import CategoryForm, ContactForm
from .models import Category, Contact


def home_page(request):
    total_contacts = Contact.objects.count()
    categories = Category.objects.annotate(
        contact_count=Count('contacts')
    )
    return render(request, 'contacts/home.html', {
        'total_contacts': total_contacts,
        'categories': categories,
    })


def contact_list(request):
    contacts = Contact.objects.select_related('category').all()
    filter = ContactFilter(request.GET, queryset=contacts)
    contacts = filter.qs

    sort = request.GET.get('sort', '-created_at')
    if sort == 'name':
        contacts = contacts.order_by('full_name')
    elif sort == '-name':
        contacts = contacts.order_by('-full_name')
    elif sort == 'created_at':
        contacts = contacts.order_by('created_at')
    else:
        contacts = contacts.order_by('-created_at')

    paginator = Paginator(contacts, 10)
    page = request.GET.get('page')
    try:
        contacts_page = paginator.page(page)
    except (PageNotAnInteger, EmptyPage):
        contacts_page = paginator.page(1)

    categories = Category.objects.all()
    category_id = request.GET.get('category')
    search_query = request.GET.get('search')
    return render(request, 'contacts/contact_list.html', {
        'contacts': contacts_page,
        'categories': categories,
        'selected_category': int(category_id) if category_id else None,
        'search_query': search_query or '',
        'current_sort': sort,
    })


def contact_detail(request, pk):
    contact = get_object_or_404(
        Contact.objects.select_related('category'), pk=pk
    )
    return render(request, 'contacts/contact_detail.html', {
        'contact': contact,
    })


def add_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Contact added successfully!')
            return redirect('contact_list')
    else:
        form = ContactForm()
    return render(request, 'contacts/contact_form.html', {
        'form': form, 'title': 'Add Contact',
    })


def update_contact(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES, instance=contact)
        if form.is_valid():
            form.save()
            messages.success(request, 'Contact updated successfully!')
            return redirect('contact_detail', pk=contact.pk)
    else:
        form = ContactForm(instance=contact)
    return render(request, 'contacts/contact_form.html', {
        'form': form, 'title': 'Edit Contact', 'contact': contact,
    })


def delete_contact(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        contact.delete()
        messages.success(request, 'Contact deleted successfully!')
        return redirect('contact_list')
    return render(request, 'contacts/contact_confirm_delete.html', {
        'contact': contact,
    })


def category_list(request):
    categories = Category.objects.annotate(
        contact_count=Count('contacts')
    ).all()
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Category added successfully!')
            return redirect('category_list')
    else:
        form = CategoryForm()
    return render(request, 'contacts/category_list.html', {
        'categories': categories,
        'form': form,
    })
