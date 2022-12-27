using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.IO;
using System.Text.RegularExpressions;

namespace Easm
{
    class Program
    {
        static void Main(string[] args)
        {
            bool debug = false;
            bool binary = false;
            bool interactive = false;
            bool command = false;
            string file = null;
            if (args.Length > 0)
            {
                if (args[0] == "-d" || args[0] == "--debug")
                {
                    debug = true;
                    args = args.Skip(1).ToArray();
                }
                if (args[0] == "-b" || args[0] == "--binary")
                {
                    binary = true;
                    args = args.Skip(1).ToArray();
                }
                if (args[0] == "-c" || args[0] == "--command")
                {
                    command = true;
                    args = args.Skip(1).ToArray();
                }
                if (args.Length > 0)
                {
                    file = args[0];
                }
            }
            if (file != null)
            {
                if (debug)
                {
                    Console.WriteLine("Easm - Debug Mode:");
                }
                else
                {
                    Console.WriteLine("Easm:");
                }
                if (binary)
                {
                    Console.WriteLine("Binary not implemented!");
                }
                else
                {
                    string[] readlines = File.ReadAllLines(file);
                    List<string> proglines = new List<string>();
                    foreach (string x in readlines)
                    {
                        if (x != "")
                        {
                            if (!x.StartsWith(";"))
                            {
                                proglines.Add(x);
                            }
                        }
                    }
                    List<List<string>> prog = new List<List<string>>();
                    List<List<string>> oprog = new List<List<string>>();
                    int r = 0;
                    foreach (string line in proglines)
                    {
                        prog.Add(new List<string>());
                        string[] s = Regex.Split(line, @"\s+");
                        foreach (string com in s)
                        {
                            prog[r].Add(com);
                        }
                        r++;
                    }
                    oprog = prog.Select(x => x.ToList()).ToList();
                    if (prog.Count > 0)
                    {
                        r = 0;
                        foreach (List<string> item in prog)
                        {
                            if (prog[r].First() == ":")
                            {
                                label();
                            }
                            r++;
                        }
                        r = 0;
                        prog = oprog.Select(x => x.ToList()).ToList();
                        while (r < prog.Count)
                        {
                            evaleasm();
                            r++;
                        }
                    }
                }
            }
            else
            {
                if (debug)
                {
                    Console.WriteLine("Easm Interactive - Debug Mode:");
                }
                else
                {
                    Console.WriteLine("Easm Interactive:");
                }
                while (true)
                {
                    List<List<string>> prog = new List<List<string>>();
                    prog.Add(new List<string>());
                    string line = Console.ReadLine();
                    string[] s = Regex.Split(line, @"\s+");
                    foreach (string com in s)
                    {
                        prog[0].Add(com);
                    }
                    if (prog[0].Count > 0)
                    {
                        r = 0;
                        evaleasm();
                    }
                }
            }
        }
        static int tonum(string num)
        {
            try
            {
                return int.Parse(num);
            }
            catch
            {
                return -1;
            }
        }
        static string tostr(string txt)
        {
            if (txt.StartsWith("\"") && txt.EndsWith("\""))
            {
                return txt.Substring(1, txt.Length - 2);
            }
            else
            {
                return null;
            }
        }
        static bool iscom(string com)
        {
            if (coms.ContainsKey(com))
            {
                return true;
            }
            else
            {
                return false;
            }
        }
        static bool isintvar(string statement)
        {
            if (int_vars.ContainsKey(statement))
            {
                return true;
            }
            else
            {
                return false;
            }
        }
        static bool isstrvar(string statement)
        {
            if (str_vars.ContainsKey(statement))
            {
                return true;
            }
            else
            {
                return false;
            }
        }
        static void raiseerror(string err)
        {
            Console.Error.WriteLine("Error: " + err);
            Environment.Exit(1);
        }
        static dynamic evaleasm()
        {
            string statement = prog[r].First();
            prog[r].RemoveAt(0);
            if (command)
            {
                Console.WriteLine("statement: " + statement);
            }
            int isnum = tonum(statement);
            string isstr = tostr(statement);
            bool is_com = iscom(statement);
            bool is_strvar = isstrvar(statement);
            bool is_intvar = isintvar(statement);
            if (debug)
            {
                Console.WriteLine("statement: " + statement + " is command: " + is_com + " is string: " + isstr + " is num: " + isnum + " is str var: " + is_strvar + " is int var: " + is_intvar + " int stack: " + int_stack + " str stack: " + str_stack + " str vars: " + str_vars + " int vars: " + int_vars + " labels: " + labels + " is if " + is_if);
            }
            if (isnum != -1)
            {
                int_stack.Add(isnum);
            }
            else if (isstr != null)
            {
                str_stack.Add(isstr);
            }
            else if (is_com)
            {
                coms[statement]();
            }
            else if (is_strvar)
            {
                str_stack.Add(str_vars[statement]);
            }
            else if (is_intvar)
            {
                int_stack.Add(int_vars[statement]);
            }
        }
        static int r = 0;
        static List<string> str_stack = new List<string>();
        static List<int> int_stack = new List<int>();
        static Dictionary<string, string> str_vars = new Dictionary<string, string>();
        static Dictionary<string, int> int_vars = new Dictionary<string, int>();
        static Dictionary<string, int> labels = new Dictionary<string, int>();
        static bool is_if = true;
        static List<List<string>> prog = new List<List<string>>();
        static List<List<string>> oprog = new List<List<string>>();
        static Dictionary<string, dynamic> coms = new Dictionary<string, dynamic>()
        {{"pushint",pushint}, {"pushstr",pushstr},{"pullint",pullint},{"pullstr",pullstr},{"peekint",peekint},
            {"peekstr",peekstr},
            {"string",estring},
            {"int",toint},
            {"concat",concat},
            {"show",show},
            {"add",add},
            {"mult",mult},
            {"div",div},
            {"exit",exitprog},
            {"intvar",intvar},
            {"strvar",strvar},
            {"ask",ask},
            {"if",eif},
            {"else",eelse},
            {"eq",eq},
            {"not",enot},
            {":",label},
            {"goto",egoto},
            {"{",startbrace},
            {"}",endbrace},
            {"concats",concats},
            {"adds",adds},
            {"use",use},
            {"rand",err_rand},
            {">",more},
            {"<",less}
        };
        static void pushint()
        {
            int statement = evaleasm();
            if (statement != -1)
            {
                int_stack.Add(statement);
            }
            else
            {
                raiseerror("Error in pushint!");
            }
        }
        static void pushstr()
        {
            string statement = evaleasm();
            if (statement != null)
            {
                str_stack.Add(statement);
            }
            else
            {
                raiseerror("Error in pushstr!");
            }
        }
        static int pullint()
        {
            return int_stack.Last();
        }
        static string pullstr()
        {
            return str_stack.Last();
        }
        static int peekint()
        {
            return int_stack[int_stack.Count - 2];
        }
        static string peekstr()
        {
            return str_stack[str_stack.Count - 2];
        }
        static string estring()
        {
            return evaleasm().ToString();
        }
        static int toint()
        {
            int statement = evaleasm();
            if (statement != -1)
            {
                return statement;
            }
            else
            {
                raiseerror("Error in int!");
                return -1;
            }
        }
        static int add()
        {
            return int_stack[int_stack.Count - 1] + int_stack[int_stack.Count - 2];
        }
        static int adds()
        {
            int one = evaleasm();
            int two = evaleasm();
            if (one != -1 && two != -1)
            {
                return one + two;
            }
            else
            {
                raiseerror("Error in adds!");
                return -1;
            }
        }
        static int mult()
        {
            return int_stack[int_stack.Count - 1] * int_stack[int_stack.Count - 2];
        }
        static int mults()
        {
            int one = evaleasm();
            int two = evaleasm();
            if (one != -1 && two != -1)
            {
                return one * two;
            }
            else
            {
                raiseerror("Error in mults!");
                return -1;
            }
        }
        static string div()
        {
            return (int_stack[int_stack.Count - 1] / int_stack[int_stack.Count - 2]).ToString();
        }
        static string divs()
        {
            int one = evaleasm();
            int two = evaleasm();
            if (one != -1 && two != -1)
            {
                return (one / two).ToString();
            }
            else
            {
                raiseerror("Error in divs!");
                return null;
            }
        }
        static string concat()
        {
            return str_stack[str_stack.Count - 2] + str_stack[str_stack.Count - 1];
        }
        static string concats()
        {
            string one = evaleasm();
            string two = evaleasm();
            if (one != null && two != null)
            {
                return one + two;
            }
            else
            {
                raiseerror("Error in concats!");
                return null;
            }
        }
        static void strvar()
        {
            string var_name = evaleasm();
            string statement = evaleasm();
            if (statement != null)
            {
                str_vars.Add(var_name, statement);
            }
            else
            {
                raiseerror("Error in strvar!");
            }
        }
        static void intvar()
        {
            string var_name = evaleasm();
            int statement = evaleasm();
            if (statement != -1)
            {
                int_vars.Add(var_name, statement);
            }
            else
            {
                raiseerror("Error in intvar!");
            }
        }
        static void eif()
        {
            if (evaleasm() == 1)
            {
                is_if = true;
                evaleasm();
            }
            else
            {
                is_if = false;
            }
        }
        static void eelse()
        {
            if (!is_if)
            {
                evaleasm();
                is_if = true;
            }
        }
        static int eq()
        {
            int one = evaleasm();
            int two = evaleasm();
            if (one == two)
            {
                return 1;
            }
            else
            {
                return 0;
            }
        }
        static int enot()
        {
            if (evaleasm() == 0)
            {
                return 1;
            }
            else
            {
                return 0;
            }
        }
        static string ask()
        {
            return Console.ReadLine();
        }
        static void startbrace()
        {
            while (evaleasm() != endbraces)
            {
            }
        }
        static string endbrace()
        {
            return endbraces;
        }
        static int more()
        {
            int one = evaleasm();
            int two = evaleasm();
            if (one > two)
            {
                return 1;
            }
            else
            {
                return 0;
            }
        }
        static int less()
        {
            int one = evaleasm();
            int two = evaleasm();
            if (one < two)
            {
                return 1;
            }
            else
            {
                return 0;
            }
        }
        static void use()
        {
            string name = evaleasm();
            if (name == "rand")
            {
                coms.Add("rand", rand);
            }
        }
        static int rand()
        {
            int one = evaleasm();
            int two = evaleasm();
            if (one != -1 && two != -1)
            {
                Random rnd = new Random();
                return rnd.Next(one, two);
            }
            else
            {
                raiseerror("Error in rand!");
                return -1;
            }
        }
        static void err_rand()
        {
            raiseerror("You are not using rand!");
        }
        static void label()
        {
            string name = evaleasm();
            int line = r;
            labels.Add(name, line);
        }
        static void egoto()
        {
            string name = evaleasm();
            if (labels.ContainsKey(name))
            {
                r = labels[name];
                prog = oprog.Select(x => x.ToList()).ToList();
            }
            else
            {
                raiseerror("Error in goto!");
            }
        }
        static void show()
        {
            string statement = evaleasm();
            if (statement != null)
            {
                Console.Write(statement);
            }
            else
            {
                raiseerror("Error in show!");
            }
        }
        static string endbraces = "endbraces";
    }
}
