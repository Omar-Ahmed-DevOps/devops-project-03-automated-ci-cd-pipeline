from app import add

def test_add_failure():
    # بنجبر الاختبار يفشل بشكل قاطع عن طريق مقارنة خاطئة تماماً
    assert add(2, 3) == 500, "فشل مقصود: المفروض الناتج 5 مش 500!"
