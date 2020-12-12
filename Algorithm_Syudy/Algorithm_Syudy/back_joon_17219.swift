//
//  back_joon_17219.swift
//  Algorithm_Syudy
//
//  Created by Minseop Kim on 2020/12/12.
//

import Foundation

class BackJoon17219 {
    var N: Int = 0
    var M: Int = 0
    
    var webDict: Dictionary = [String: String]()
    
    func inputWebPassword() {
        for _ in stride(from: 0, to: self.N, by: 1) {
            let web = readLine()!.components(separatedBy: " ")
            self.webDict.updateValue(web[1], forKey: web[0])
        }
    }
    
    func getAnswer() {
        for _ in stride(from: 0, to: self.M, by: 1) {
            let address = readLine()!
            print(self.webDict[address]!)
        }
    }
    
    func firstInput() {
        let arr = readLine()!.components(separatedBy: " ").map({ (value) in Int(value)! })
        self.N = arr[0]
        self.M = arr[1]
    }

}





