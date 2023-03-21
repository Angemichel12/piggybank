from django.db.models import Sum, Avg, Count
from .models import Transaction, Category
from dataclasses import dataclass
from decimal import Decimal

@dataclass
class ReportEntry:
    category: Category
    total: Decimal
    count: int
    avg: Decimal

def transactions_reports():
    data = []
    queryset = Transaction.objects.values("category").annotate(total=Sum("amount"),
                                                               count=Count("id"),
                                                               avg=Avg("amount"))
    categories_index = {}
    for category in Category.objects.all():
        categories_index[category.pk]= category
    for entry in queryset:
        category = categories_index.get(entry["category"])
        report_entry = ReportEntry(category, entry["total"], entry["count"], entry["avg"])
        data.append(report_entry)
    return data