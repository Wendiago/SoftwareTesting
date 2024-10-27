
## Software testing life cycle
**Phases of STLC**: 3 bước đầu là Preparation, 3 bước sau là Execution
* Requirement Analysis 
* Test planning
* Test case design: Chưa có phần mềm hỗ trợ, là bước khó nhất 
* Environment Setup 
* Test execution: Nếu có lỗi => Test report
* Test cycle closure: Báo cáo thống kê

**1. Requirement analysis**
- Phân tích và hiểu scope của testing => Làm việc với BA => QUAN TRỌNG
- Xây dựng "Requirement Traceability Matrix" (RTM): Ma trận truy vết:
    * Truy ra: requirement này có bao nhiêu testcase, testcase này có bao nhiêu requirement
- Đánh giá khả năng automation testing

=> Input (Entry criteria): Requirement specification, Application Architecture
=> Output (Deliverables): Requirement Traceability Matrix, Automation Feasibility Report

**2. Test planning**
- Scope: Xác định những tính năng đc test và những tính năng không được test
- Strategy: Chiến lược test = level + type + tool (method)
- Environment
- Schedule: 
    * Time and cost
    * Test deliverables and milestones 
    * Assign roles and responsibility

=> Input (Entry criteria): Project plan, Acceptance criteria , requirement specification
=> Output (Deliverables): Test plan

**3. Test case design**
- Design test case + generate data (test case = step + data)
- Create automation script (if applicable) => Dùng cho automation test
- Update RTM
- Test cases: 
    * Inputs
    * Test steps
    * Expected result 
=> Input (Entry criteria): Test plan, requirement specification

**4. Environment setup**
- Chuẩn bị danh sách phần cứng và phần mềm
- Configure và deploy enviroment
=> Input: Test Plan, test cases, system architecture
=> Output: Fully functional test env, Smoke test results

**5. Test execution**
- Chạy test cases trong môi trường đã deploy
- Thu thập và phân tích kết quả test
- So sánh kết quả thu được với expected result
- Report defects found
=> Input: Cases, data, automation script
=> Output: Report

**6. Test cycle closure**
- Đảm bảo mọi hoạt động đã hoàn thành
- Document test process
- Prepare test summary report (tổng hợp, kiếm đc bao nhiêu bug, bao nhiêu lỗi lớn nhỏ, đã đc fix chưa...)
- Prepaê test closure report (rút kinh nghiệm, góp ý)

**Exercise**: Testing a simple fraction calculator in console: The input consists of 2 fractions, each fraction has the format 
"numerator/denominator", are integers, denominator cannot be zero.
There are 4 operations +, -, *, /
The result must be simplest form, eliminate the negative denominator, if the result is an improper fraction, it should also be represented as 
a mixed number

**Valid test cases (Positive test cases)**:
- các trường hợp + - * /
    * 1/2 1/4 + => 3/4
    * 1/2 1/4 - => 3/4
    * 1/2 1/4 * => 3/4
    * 1/2 1/4 / => 3/4
- Các kết quả là số nguyên => 1 thì phải là 1/1
    * 1/1 0/1 + => 1/1
- Rút gọn phân số
    * 2/4 2/4 + => 1/1
- Nếu kết quả có tử > mẫu => kết quả là hỗn số, vd: 3/2 = 1 1/2

**Invalid test cases (Negative test cases)**:
- Mãu phân số 1 là zero, Mẫu phân số 2 là 0 
- Tử hoặc mẫu tràn số (tử 1, mẫu 1, tử 2, mẫu 2) 
- Kết quả tràn số 
- Tử có kí tự đặc biệt, Mẫu có kí tự đặc biệt
- Operator không thuộc 1 trong 4 phép + - * /
- Không nhập phân số 1, không nhập phân số 2 
- Không nhập tử 1/ mẫu 1/ tử 2/ mẫu 2
- Không có dấu / trong phân số
- Có nhiều hơn 1 dấu / trong phân số 


## 7 PRINCIPLES OF SOFTWARE TESTING
- Testing **shows** the presence of defects 
=> Mục tiêu của kiểm thử phần mềm là tìm ra lỗi, không phải chứng minh phần mềm không có lỗi
=> Phần mềm luôn luôn có lỗi

- **Exhaustive testing** is not possible 
=> Không thể vét cạn tất cả các lỗi
=> Cần test một lượng hợp lí

- **Early** testing
=> Kiểm thử sớm nhất có thể. Kiểm thử ngay trên requirement
=> Lỗi phát hiện càng sớm thì chi phí fix càng rẻ

- Defect **clustering** (gom nhóm lỗi)
=> Chỉ có 20% modules chứa 80% tất cả các lỗi
=> Tập trung test các module quan trọng

- Pesticide **paradox**
=> Nghịch lý thuốc trừ sâu: Sử dụng cùng 1 phương pháp sẽ không phát hiện được lỗi mới

- Testing is **context dependent**
=> Ứng với các ngữ cảnh khác nhau chúng ta phải áp dụng các phương pháp kiểm thử khác nhau

- Absence of error - **fallacy** (validation)
=> Có khả năng phần mềm 99% không lỗi vẫn không dùng được
=> Kiểm thử không phải chỉ là tìm lỗi, mà phải đảm bảo hoạt động đúng requirement


## LEVELS OF SOFTWARE TESTING
- 4 Levels: Unit, Integration, System, Acceptance
- 
**1. Unit test (Component test, Module test, Programming test)** 
- Test Individual Component: test độc lập
- Bug is fixed immediately, no need to report
=> Developer tự test

Mock object: Là đối tượng giả lập để test. Gồm 2 loại Stubs và Drivers
Ví dụ: 
- Muốn test đối tượng A mà A phải gọi đối tượng B, ta phải tạo một đối tượng giả thay cho B gọi là Stubs
- Ngược lại muốn test đối tượng B được A gọi, ta tạo ra một đối tượng giả thay cho A gọi là Drivers 

**2. Integration test**
- Test components work together (2 units trở lên)
- Test the interface/interaction between units
=> Developer + Tester cùng làm
- Có 2 hướng tiếp cận:
    * Big-bang integration: gắn tất cả component lại với nhau, tương tự như system test 
    => nhanh gọn dễ
    => tuy nhiên không biết lỗi ở chỗ nào, phải chờ tất cả các component hoàn thành, không thể ưu tiên test unit nào quan trọng 
    
    * Incremental integration: Bắt đầu từ 1 component, gắn thêm từng phần một
    => Có 3 hướng tiếp cận: 
       - Top-down: Deep first inte, Breath first inte => Đi từng tổng quan tới chi tiết
       - Bottom-up: Đi từ thành phần con tới tổng quát
       - Sandwich: Kết hợp 2 phương pháp trên

**3. System test**
- Là bước cuối cùng của integration testing
=> Tester và BA thực hiện

**4. Acceptance test** 
- Bước cuối cùng của validation
- Đảm bảo hệ thống đạt được yêu cầu khách hàng
=> User test 
- Kiểm thứ Alpha quy mô nhỏ trước, sau đó kiểm thử Beta trên diện rộng: 
    * Alpha testing: Kiểm thử trên môi trường development => tập trung vào phần mềm 
    * Beta testing: Kiểm thử trên môi trường thực tế
  

## TYPES OF SOFTWARE TESTING
- Functional testing: kiểm tra phần mềm hoạt động đúng
    * Là black box testing
    * Không cần quan tâm tới cách implement
    
- Non functional testing: kiểm tra phần mềm hoạt động thế nào dưới các điều kiện nhất định (hoạt động tốt)
    * Performance testing: stress testing, endurance testing, load testing, spike testing. 
    * Usability: giao diện
    * Security
    * Configuration/Installation
    * Recovery
    
- Structural testing: 
    * Là white box testing
    * Code coverage: 
        - Statement coverage: chạy tất cả các dòng lệnh
        - Decision coverage
        - Condition coverage
        - Path coverage
        - Loop coverage
        
- Change-related testing
    * Re-testing/Confirmation testing: Kiểm tra lỗi đã được sửa hay chưa
    * Regression testing:
        - Kiểm lại các trường hợp đã passed trước đó
        - Tìm ra các lỗi mới
