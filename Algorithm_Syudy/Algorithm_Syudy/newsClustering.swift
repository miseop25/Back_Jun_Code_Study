//
//  newsClustering.swift
//  Algorithm_Syudy
//
//  Created by Minseop Kim on 2022/03/09.
//

import Foundation

class News
{
    var dic1 = [String : Int]()
    var dic2 = Dictionary<String,Int>()
    
    var str1 = ""
    var str2 = ""
    init(inStr1 : String , inStr2 : String){
        str1 = inStr1.lowercased()
        str2 = inStr2.lowercased()
        makeSet()
    }
    
    func makeSet(){
        var tempStr = ""
        for val in str1{
            guard let ascii = val.asciiValue else {continue}
            if ascii < 97 || ascii > 122 {
                tempStr = ""
                continue
            }
            tempStr += String(val)
            if tempStr.count == 2 {
                if dic1[tempStr] != nil {
                    dic1[tempStr]! += 1
                }else {
                    dic1[tempStr] = 1
                }
                tempStr = String(val)
            }
        }
        tempStr = ""
        for val in str2{
            guard let ascii = val.asciiValue else {continue}
            if ascii < 97 || ascii > 122 {
                tempStr = ""
                continue
            }
            tempStr += String(val)
            
            if tempStr.count == 2 {
                if dic2[tempStr] != nil {
                    dic2[tempStr]! += 1
                }else {
                    dic2[tempStr] = 1
                }
                tempStr = String(val)
            }
        }
    }
    
    func findZaKadeNum() -> Int{
        var unionCnt = 0
        var insertCnt = 0
        
        var unionSet = Set(dic1.keys)
        for k in dic2.keys{
            unionSet.insert(k)
        }
        
        for k in unionSet {
            if (dic1[k] != nil) && (dic2[k] != nil) {
                unionCnt += max(dic1[k]!, dic2[k]!)
                continue
            }
            if dic1[k] != nil{
                unionCnt += dic1[k]!
                continue
            }
            if dic2[k] != nil {
                unionCnt += dic2[k]!
            }
        }
        
        for k in dic1.keys {
            if dic2[k] != nil {
                insertCnt += min(dic1[k]! , dic2[k]!)
            }
        }
        
        if unionCnt == 0 && insertCnt == 0 {
            return 65536
        }
        
        return Int(65536.0 * Double(insertCnt)/Double(unionCnt))
    }
    
    func getAnswer() -> Int {
        let answer = findZaKadeNum()
        return answer
    }
}

func solution(_ str1:String, _ str2:String) -> Int {
    let n = News(inStr1: str1, inStr2: str2)
    return n.getAnswer()
}
