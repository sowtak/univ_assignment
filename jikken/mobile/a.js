function to_hex(decimal) {
    if (decimal>=0 && decimal<=255) return decimal.toString(16);
    else return 0;
  }

  var n = 16;	   //二次元配列の行、列の要素数(16×16の配列を作る)
   var tableData = new Array(n);
   for(i = 0; i < n; i++) {
     tableData[i] = new Array(n);
   }

   for(var i=0;i<n;i++) {
     for(var j=0;j<n;i++) {
       if(i==0&&j==0)tableData[i][j]="\\";
       else if(i==0&&j!=0)tableData[i][j]=to_hex(j);
       else if(i!=0&&j==0)tableData[i][j]=to_hex(i);
       else tableData[i][j]=to_hex(i*j);
     }
   }
   

  document.write("<table class='border' border='1' cellpadding='3'>");  //表の定義を開始、以降のコードで表の中身を定義していく
  for(var i=0; i<n; i++){
    document.write("<tr>");  //表の横一行部分の定義を開始
    for(var j=0; j<n; j++) {
      if(i==0&&j==0)document.write('<th>',tableData[0][0] ,'</th>');
      else if(i==0&&j!=0)document.write('<th>',tableData[i][j],'</th>');
      else if(i!=0&&j==0)document.write('<th>',tableData[i][j],'</th>');
      else document.write("<td>",tableData[i][j],"</td>");
     }
    document.write("</tr>");  //表の横一行部分の定義を終了
  }
  document.write("</table>"); 　//表の定義を終了