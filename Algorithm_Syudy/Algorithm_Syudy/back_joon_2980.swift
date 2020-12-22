//
//  back_joon_2980.swift
//  Algorithm_Syudy
//
//  Created by Minseop Kim on 2020/12/22.
//

import Foundation

class BackJoon2980 {
    private var M: Int = 0
    private var N: Int = 0
    
    var time: Int = 0
    var dis: Int = 0
    var signArray: Array<Array<Int>> = []
    
    func firstInput() {
        guard let word = readLine() else {return}
        let arr = word.components(separatedBy: " ").map({ (value) in Int(value)! })
        N = arr[0]
        M = arr[1]
        for _ in 0..<N {
            signInput()
        }
    }
    
    func signInput() {
        guard let world = readLine() else {return}
        let arr = world.components(separatedBy: " ").map({(value) in
            Int(value)!
        })
        signArray.append(arr)
    }
    
    func checkRed(R: Int, G: Int) -> Int {
        let temp = time % (R+G)
        if temp < R {
            return R - temp
        }else {
            return 0
        }
    }
    
    func getAnswer() {
        signArray.forEach { (arr) in
            time += (arr[0] - dis)
            dis = arr[0]
            time += checkRed(R: arr[1], G: arr[2])
        }
        time += M - dis
        print(time)
    }
    
    
}
