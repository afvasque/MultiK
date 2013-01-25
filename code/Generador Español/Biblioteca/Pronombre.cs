using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace Biblioteca
{
    [Serializable]
    public class Pronombre:Palabra
    {
        public Pronombre(string[] silabas)
            : base(silabas)
        {
        }
    }
}
