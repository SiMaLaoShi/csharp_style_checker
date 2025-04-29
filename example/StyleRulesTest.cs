using System;
using System.Collections.Generic;
using System.Text;
using System.Linq;

// 错误的接口命名（不以I开头）
public interface resource
{
    void LoadResource();
    void UnloadResource();
}

// 正确的接口命名
public interface IResource
{
    void LoadResource();
    void UnloadResource();
}

// 错误的结构体命名（不以st开头）
public struct Point
{
    public int X;
    public int Y;
}

// 正确的结构体命名
public struct stPoint
{
    public int X;
    public int Y;
}

// 错误的类名（不符合PascalCase）
public class badPlayer {  // 同时违反了大括号规则
    // 常量命名错误（不是全大写）
    public const int maxPlayers = 4;
    public const float DefaultSpeed = 5.0f;
    
    // 正确的常量命名
    public const int MAX_PLAYERS = 4;
    public const float MAX_SPEED = 10.0f;
    
    // 私有字段命名错误（没有下划线前缀）
    private int health;
    private float speed;
    
    // 正确的私有字段命名
    private int _health;
    private float _speed;
    
    // 静态字段命名错误（没有使用s_+类型缩写格式）
    private static int playerCount;
    private static Dictionary<int, string> playerNames;
    
    // 正确的静态字段命名
    private static int s_iPlayerCount;
    private static Dictionary<int, string> s_dictPlayerNames;
    
    // 方法命名错误（不符合PascalCase）
    public void updateHealth(int amount) {  // 同时违反了大括号规则
        _health += amount;
    }
    
    // 集合命名错误（不是复数形式）
    private List<string> item;
    private Dictionary<int, float> scoreMap;
    
    // 正确的集合命名
    private List<string> _items;
    private Dictionary<int, float> _scoreMaps;
    
    // 行过长示例（视具体设置的最大行长而定）
    public void SomeLongMethod() {
        Console.WriteLine("这是一行非常长的代码，它故意超出了规则中设置的最大行长度限制，目的是测试行长度检查规则是否能正确工作。我们期望在代码检查时这一行会被标记为违反了LineIsTooLongRule规则。");
    }
    
    // 正确的方法命名和大括号放置
    public void UpdateHealth(int amount)
    {
        _health += amount;
    }
    
    public void Update()
    {
        // if语句的大括号错误放置
        if (_health <= 0) {
            Console.WriteLine("Game Over");
        }
        
        // 正确的if语句大括号放置
        if (_speed > MAX_SPEED)
        {
            _speed = MAX_SPEED;
        }
    }
}

// 正确的类名
public class Player
{
    public void Move(float x, float y)
    {
        // 实现移动逻辑
    }
}

// 测试枚举命名
public enum direction  // 错误的枚举命名（不符合PascalCase）
{
    North,
    South,
    East,
    West
}

// 正确的枚举命名
public enum Direction
{
    North,
    South,
    East,
    West
}

// 包含各种嵌套块的示例类
public class StyleTestClass
{
    public void TestMethod()
    {
        // 错误的for循环大括号
        for (int i = 0; i < 10; i++) {
            Console.WriteLine(i);
        }
        
        // 错误的foreach循环大括号
        foreach (var item in new[] { 1, 2, 3 }) {
            Console.WriteLine(item);
        }
        
        // 错误的try-catch大括号
        try {
            throw new Exception();
        } catch (Exception ex) {
            Console.WriteLine(ex.Message);
        } finally {
            Console.WriteLine("Finally");
        }
    }
}
