//
//  back_joon_1931.swift
//  Algorithm_Syudy
//
//  Created by Minseop Kim on 2022/05/18.
//

import Foundation


class MeetingRoom {
    
    var timeDict: [Int : Int] = [:]
    var startTime = 0
    var endTime = 0
    init(){
        let input = readLine()!
        let n = Int(input)!
        for i in 0..<n {
            var arr :[Int] = []
            if let word = readLine() {
                arr = word.components(separatedBy: " ").map({ (value) in Int(value)! })
                if (timeDict[arr[0]] == nil) {
                    timeDict[arr[0]] = arr[1]
                }else {
                    if timeDict[arr[0]]! > arr[1] { timeDict[arr[0]] = arr[1] }
                }
                    
                
                if i == 0 {
                    startTime = arr[0]
                    endTime = arr[1]
                }else {
                    if startTime > arr[0] { startTime = arr[0] }
                    if endTime < arr[1] { endTime = arr[1] }
                }
            }
        }
    }
    
    func checkTime(time : Int) -> Int{
        var cnt = 0
        var t = time
        while t < endTime {
            if (timeDict[t] != nil) {
                t = timeDict[t]!
                cnt += 1
            }else {
                t += 1
            }
        }
        return cnt
    }
    
    func getAnswer() -> Int {
        
        var answer = 0
        let keys = timeDict.keys
        let keyList = keys.sorted(by: <)
        for k in keyList {
            let temp = checkTime(time: k)
            if temp > answer { answer = temp }
        }
        return answer
    }
    
    
}


//let mr = MeetingRoom()
//print(mr.getAnswer())
