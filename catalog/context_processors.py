from catalog.models import (SPECIAL_MODEL_SLUG, TRACTIVE_UNIT_MODEL_SLUG, TRAILER_MODEL_SLUG, TRUCK_MODEL_SLUG)

def catalog(request):
    return {
        'SPECIAL_MODEL_SLUG': SPECIAL_MODEL_SLUG,
        'TRACTIVE_UNIT_MODEL_SLUG': TRACTIVE_UNIT_MODEL_SLUG,
        'TRAILER_MODEL_SLUG': TRAILER_MODEL_SLUG,
        'TRUCK_MODEL_SLUG': TRUCK_MODEL_SLUG
    }