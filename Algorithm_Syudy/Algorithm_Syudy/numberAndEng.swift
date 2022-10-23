//
//  numberAndEng.swift
//  Algorithm_Syudy
//
//  Created by Minseop Kim on 2022/03/01.
//

import Foundation

class NumAndEng{
    private var numDict = Dictionary<String, String>()
    var originStr :String = ""
    var answer = ""
    let number: Set<Character> = ["1","2", "3", "4", "5", "6", "7", "8", "9", "0"]
    
    init(Str : String)
    {
        originStr = Str
        initDict()
    }
    
    func initDict(){
        numDict["one"]      =   "1"
        numDict["two"]      =   "2"
        numDict["three"]    =   "3"
        numDict["four"]     =   "4"
        numDict["five"]     =   "5"
        numDict["six"]      =   "6"
        numDict["seven"]    =   "7"
        numDict["eight"]    =   "8"
        numDict["nine"]     =   "9"
        numDict["zero"]     =   "0"
    }
    
    func getAnswer() -> String {
        var tempStr = ""
        for c in originStr
        {
            tempStr += String(c)
            if number.contains(c){
                answer += String(c)
                tempStr = ""
                continue
            }
            if let key = numDict[tempStr]{
                answer += key
                tempStr = ""
            }
        }
        
        return answer
    }
    
    
}


func solution(_ s:String) -> Int {
    var sol = NumAndEng(Str: s)
    let answer = sol.getAnswer()
    return Int(answer) ?? 0
}
