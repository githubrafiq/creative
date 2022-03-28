from django.shortcuts import render, redirect

# Create your views here.
def python(request):
    return render(request, 'assignment_01/python.html')

def ass1_home(request):
    if request.method == 'POST':
        try:
            choice = request.POST["choice"]
        except:
            return redirect('ass1-home')

        if choice:
            if choice == 'fixed':
                return redirect('fixed')

            if choice == 'range':
                return redirect('range')

            if choice == 'random':
                return redirect('random')
            
    return render(request, 'assignment_01/ass1_home.html')

# ---------------------start class Mymethods-----------------------------------------
class MyMethods:
    def __init__(self, nums):
        self.nums = nums
    
    def numCopy(self):
        x = self.nums.copy()
        return x
        
    def find_length(self):
        length = len(self.nums)
        return length 
    
    def find_even(self):
        even = []
        for n in self.nums:
            if int(n) % 2 == 0:
                even.append(n)
                even.sort()
        return even

    def find_odd(self):
        odd = []
        for n in self.nums:
            if int(n) % 2 != 0:
                odd.append(n)
                odd.sort()
        return odd

    def find_min(self):
        self.nums.sort()
        min = self.nums[0]
        return min

    def find_max(self):
        self.nums.sort(reverse=True)
        max = self.nums[0]
        return max

    def find_sum(self):
        sum = 0
        for i in self.nums:
            sum += i
        return sum

    def find_avg(self):
        sum = 0
        for i in self.nums:
            sum += i
        avg = sum / len(self.nums)
        return avg
# ---------------------end class Mymethods-----------------------------------------


def mycontext(n):
    x = MyMethods(n)
    ctx = {
        'nums': x.numCopy(),
        'length': x.find_length(),
        'even': x.find_even(),
        'odd': x.find_odd(),
        'min': x.find_min(),
        'max': x.find_max(),
        'sum': x.find_sum(),
        'avg': x.find_avg(),
    }
    return ctx
def fixed(request):
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    if request.method == 'POST':
        context = {
            'obj': mycontext(nums)
        }
        
        return render(request, 'assignment_01/fixed.html', context)
    return render(request, 'assignment_01/fixed.html', {'nums': nums})


def myRange(request):
    if request.method == 'POST':
        try:
            val = int(request.POST['mynum'])
        except:
            return redirect('range')
    
        nums = []
        for i in range(val + 1):
            nums.append(i)
        
        
        x = MyMethods(nums)
        context = {
            'nums': x.numCopy(),
            'length': x.find_length(),
            'even': x.find_even(),
            'odd': x.find_odd(),
            'min': x.find_min(),
            'max': x.find_max(),
            'sum': x.find_sum(),
            'avg': x.find_avg(),
        }
        return render(request, 'assignment_01/range.html', context)
    return render(request, 'assignment_01/range.html')
       

def random(request):
    if request.method == 'POST':
        try:
            numstr = request.POST['mynum']
        except:
            return redirect('random')


        if numstr:
            numsplit = numstr.split(', ')
            nums = []

            for char in numsplit:
                if char.isdigit():
                    nums.append(int(char))
            

            x = MyMethods(nums)
            context = {
                'nums': x.numCopy(),
                'length': x.find_length(),
                'even': x.find_even(),
                'odd': x.find_odd(),
                'min': x.find_min(),
                'max': x.find_max(),
                'sum': x.find_sum(),
                'avg': x.find_avg(),
            }
            return render(request, 'assignment_01/random.html', context)
    return render(request, 'assignment_01/random.html')

        