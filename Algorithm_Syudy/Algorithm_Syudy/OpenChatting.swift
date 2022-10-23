//
//  OpenChatting.swift
//  Algorithm_Syudy
//
//  Created by Minseop Kim on 2022/03/10.
//

import Foundation

class OpenChating
{
    var cmdQue = [(String,String)]()
    var User = [String : String]()
    var originRecord = [String]()
    var answer = [String]()
    
    
    init(record : [String]){
        originRecord = record
        checkRecord()
    }
    
    func checkRecord(){
        for str in originRecord{
            let cmds = str.components(separatedBy: " ")
            if cmds[0] == "Enter" {
                User[cmds[1]] = cmds[2]
                cmdQue.append((cmds[0], cmds[1]))
            }else if cmds[0] == "Leave" {
                cmdQue.append((cmds[0], cmds[1]))
            }else if cmds[0] == "Change"{
                User[cmds[1]]! = cmds[2]
            }
        }
    }
    
    func getAnswer() -> [String] {
        for cmd in cmdQue {
            if cmd.0 == "Enter"{
                let msg = "\(User[cmd.1]!)님이 들어왔습니다."
                answer.append(msg)
            }else if cmd.0 == "Leave" {
                let msg = "\(User[cmd.1]!)님이 나갔습니다."
                answer.append(msg)
            }
        }
        return answer
    }
    
}



func solution(_ record:[String]) -> [String] {
    let oc = OpenChating(record: record)
    return oc.getAnswer()
}
