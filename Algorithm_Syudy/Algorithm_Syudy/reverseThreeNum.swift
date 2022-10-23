//
//  reverseThreeNum.swift
//  Algorithm_Syudy
//
//  Created by Minseop Kim on 2022/03/01.
//

import Foundation

class ReverseThreeNum
{
    var originNum : Int = 0
    private let divNum = 3
    
    init(num : Int)
    {
        originNum = num
    }
    
    func makeTri() -> String
    {
        var result = ""
        while true
        {
            let remain = originNum % divNum
            let value = originNum / divNum
            if value == 0{
                result += String(remain)
                return result
            }
            originNum = value
            result += String(remain)
        }
    }
    
    func backToTen(triNum : String) -> Int
    {
        let len = triNum.count - 1
        var result = 0
        for (i, val) in triNum.enumerated(){
            let temp = Int(pow(Double(divNum), Double(len - i)))
            if val == "1"{
                result += temp
            }
            else if(val == "2"){
                result += (2 * temp)
            }
        }
        return result
    }
    
    func getAnswer() -> Int
    {
        let triStr = makeTri()
        return backToTen(triNum: triStr)
    }
    
}

func solution(_ n:Int) -> Int {
    let revreseThree = ReverseThreeNum(num: n)
    let result = revreseThree.getAnswer()
    return result
}
