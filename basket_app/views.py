from django.shortcuts import render

# Create your views here.

# 세션 만들기

def mainFunc(request):
    return render(request, 'main.html')


def page1Func(request):
    return render(request, 'page1.html')



def page2Func(request):
    return render(request, 'page2.html')


def cartFunc(request):
    name = request.POST["name"]
    price = request.POST["price"]
    product = {'name':name, 'price':price} # java로 말하자면 DTO
    
    productList = [] # 상품통
    
    if "shop" in request.session: # 두번째 부터 여기가 실행
        productList = request.session['shop']   # 세션 내에 'shop'이라는 키로 productList가 등록
        productList.append(product)
        request.session['shop'] = productList
        
    else:
        productList.append(product)
        request.session['shop'] = productList # 최초 상품일 경우 여기가 실행
    
    print(productList)
    
    context={} # dict type
    context['products'] = request.session['shop'] # products란 키에 담음 - request.session['shop']이거를
    
    return render(request, 'cart.html', context)

# 세션 지우기 

def buyFunc(request):
    if "shop" in request.session:
        productList = request.session['shop']
        total = 0
        
        for p in productList:
            total += int(p['price'])
        
        print('결제 총액 : ', total)
        request.session.clear() # 결제를 하면 세션의 모든 키를 삭제한다.
        
        # del request.session['shop']  # 특정 키를 가진 세션내용을 삭제
    
    return render(request, 'buy.html', {'total':total})
        
        
        
