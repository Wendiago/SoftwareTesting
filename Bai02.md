# TEST DOCUMENTATION
- Test policy: Organizational level document
- Test strategy: Program level document
- Test plan: Project level document
- Test cases
- Test reports

## TEST CASE

### Why?
- Accountability: cần có minh chứng rằng mình đã test
- Reproducibility: tính tái sử dụng 
- Tracking: tính truy vết
- Automation
- To find bugs
- To verify that tests are being executed correctly
- To measure test coverage

### Essentials
1. Tracking info
2. Test case ID
3. Test case description/name:
    - Objective / title: cho người đọc cái idea về test case này làm gì
    - Precondition
    - Test steps / script
    - Test data
    - Expected result
    - Observed results
    - Status: Pass/Fail/Block/Untest
    - Test environment
    - Bug ID
    - Comment

**Ví dụ:** Viết các test descriptions cho tính năng: 
> Moving a file from folder A to folder B
- Test moving a file from folder A to B successfully
- Test moving a file that is currently in use
- Test moving a file when there is a file with the same name in folder B
- Test moving a file when folder B reach its max capacity
- Test moving a file with insufficient permission

> Testing the inserting of a record to a table
- Test inserting a record to a table successfully
- Test inserting a record when the table doesn't have any record
- Test inserting a record when the record is null
- Test inserting a record when the record is missing required fields
- Test inserting a record with invalid data types
- Test inserting duplicate record 
- Test inserting record that has foreign key constraint
- Test inserting a record exceed field size limit
- Test inserting a record with insufficient permission

**Gợi ý đặt tên**
Test case: Objective/Title Syntax: Action + Function + Operating Condition
  1. Action: Verify, Test, Validate, Execute, Run, Print...
  2. Function: function, feature, validation point
  3. Operating Condition: data, specific condition

**Precondition**
- Để thực hiện được test case này, phải thỏa mãn điều kiện sau
VD: Đã tồn tại tài khoản này, đã đăng nhập, file/folder đã tồn tại

**Test step**
- This is the expected result
- Write it as a step
- Define clearly state: what behavior, result or point that you are attempting
to validate


## TEST REPORT
- Bug/Defect life cycle
- Bug/Defect report
- Test summary report

![Defect life cycle](/assets/Bai02//DLC.jpeg)

### Essential
1. Bug ID: định danh, khác test case ID
2. Function name: tên function có bug
3. **Problem summary**: Test Objective + Actual result (vs. Expected result). 
**Example**: There is no error message when account exists, The room price is wrong when check-in date is equal to check-out date
5. How to reproduce it: Test steps + Expected result + Actual result
=> Hướng dẫn cho dev tái hiện lại lỗi đó để fix
7. Reported by: Name/ID of the tester who report the defect
8. Date: Date when the defect is reported
9. Assign to: Name/ID of the developer who will fix the defect
10. Status: 
    - New/ Closed / Reopened
    - Rejected/ Deffered/ Duplicate / In-progress/ Fixed
11. Priority:
    - **Immediate (Critical):** The defect need to be fixed immediately or in 01 day because it may cause great damage to the product
    - **High:** The defect should be fixed within 02-04 days because it
    impacts the product’s main features
    - **Medium:** The defect should be fixed within 05-08 days because it
causes minimal deviation from the product requirement
    - **Low:** The defect will be fixed later because it has very minor
affect the product operation
13. Severity:
    - **Fatal** The defect cause great damage to the product. Ex: system crash, lost data
    - **Serious** The defect impacts the product’s main features Ex: User can delete comment without login
    - **Medium** The defect causes minimal deviation from the product requirement
Ex: The GUI of the website does not display correctly on mobile devices
    - **Cosmetic** The defect has very minor affect the product operation
Ex: Incorrect tab order, no default focus, missing short
key...

### Characteristics
- Written: phải có minh chứng đã tìm ra bug
- Numbered
- Simple: mỗi report là 1 lỗi
- Understandable: dễ hiểu
- Reproducible
- Legible
- Non-judgmental: không được quánh giá dev

### How to reproduce the defect (Tái hiện lỗi)
Record all test steps
- Keyboards and mouse activities
- Screen capture

### Test summary report
Summarize test activities and results
• Summary
• Test Case result report
• Defect Report
• Open point


## TEST PLAN
1. Analyze the product
2. Develop test strategy
- **Define scope**: quyết định những function, feature để test, những phần nào ko test
- **Identify testing type**: chọn phương pháp nào functional testing, non-func testing, structural, change-related
- **Doc risk and issues**: quản trị rủi ro => cách phòng trách và đối phó
- **Create test logistics (deliverables)**: trả về test plan, test case, test report
3. Define Test Criteria
4. Resource Planning
5. Plan Test Environment
6. Schedule & Estimation
7. Test Deliverables 