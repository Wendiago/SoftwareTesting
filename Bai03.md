- Test design methods: Các phương pháp thiết kế test case:
# METHOD 1: DOMAIN TESTING (= EQUIVALENT PARTITION + BOUNDARY VALUE ANALYSIS)

## I. General approach
1. Identify **Input & Output** variables
2. Identify **equivalence classes** for each Input & Output
    - Divide the set of possible values (domain) of the field into subsets (sub-domains – equivalence classes)
    - Xác định miền hợp lệ và miền không hợp lệ
    - Đối với set là 1 khoảng giá trị. Chọn 1 valid equivalence class nằm trong khoảng đó và 2 invalid classes nằm ngoài khoảng
    - Đối với set là các input values thì mỗi 1 input phải là 1 valid equivalence class + chọn thêm 1 invalid equivalence class (không thuộc trong set đó). 
    - Đối với điều kiện "must be" thì chia làm 2 miền: valid và invalid
3. Find a **“best representative”** for each subset
5. Best representatives of ordered fields will typically be **boundary values**
    - Chỉ dành cho input dạng khoảng
    - For each equivalence class partition, we’ll have at most, 9 test cases to execute.
    - Biên trên, biên dưới
    - Cận biên trên (UB+1), cận biên dưới (LB+1)
    - Cận biên trên (UB-1), cận biên dưới (LB-1)
    - 