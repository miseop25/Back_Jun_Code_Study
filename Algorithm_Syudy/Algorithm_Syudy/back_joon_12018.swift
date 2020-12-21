//
//  back_joon_12018.swift
//  Algorithm_Syudy
//
//  Created by Minseop Kim on 2020/12/21.
//

import Foundation

class BackJoon12018 {
    private var M: Int = 0
    private var N: Int = 0
    private var course: Array<Int> = []
    var answer: Int = 0
    
    func firstInput() {
        if let word = readLine() {
            let arr = word.components(separatedBy: " ").map({ (value) in Int(value)! })
            N = arr[0]
            M = arr[1]
        }
        for _ in 0..<N {
            courseInput()
        }
    }
    
    func courseInput() {
        guard let word = readLine() else { return }
        guard let secondWord = readLine() else {return}
        let arr = word.trimmingCharacters(in: .whitespaces).components(separatedBy: " ").map({ (value) in Int(value)! })
        var mileage = secondWord.components(separatedBy: " ").map({ (value) in Int(value)! })
        let person = arr[0]
        let total = arr[1]
        mileage.sort(by: >)
        if person < total {
            course.append(1)
        }else {
            course.append(mileage[total-1])
        }
    }
    
    func getAnswer() {
        course.sort()
        course.forEach { (point) in
            if M - point >= 0 {
                M -= point
                answer += 1
            }else {
                return
            }
        }
        print(answer)
    }

}
