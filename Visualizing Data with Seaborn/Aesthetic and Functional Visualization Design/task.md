## Advanced Design in Seaborn

### Introduction to Advanced Design

Building on the concepts introduced in the previous lesson about data arrangement, this lesson focuses on enhancing the visual appeal and clarity of plots created with Seaborn. By implementing effective design choices, visualizations can better communicate data insights and engage the audience. This involves not only organizing the data but also improving the aesthetics of the plots.
### Key Design Elements

1. **[Color Palettes](https://seaborn.pydata.org/tutorial/color_palettes.html#tools-for-choosing-color-palettes)**: Appropriate color palettes can significantly enhance the readability and attractiveness of your plots. Seaborn offers several built-in palettes that can be customized to suit the theme of your analysis.
   <img src="https://seaborn.pydata.org/_images/color_palettes_22_0.svg">

   - Example 1: Applying a *pastel* palette creates a lighter, softer tone.
     ```
          sns.set_palette("pastel")
          sns.countplot(x=x_data, hue=hue_data, data=my_data)
     ```
   - Example 2: Using a *dark*  palette provides a more formal setting for visualizing data.
     ```
          sns.set_palette("dark")
          sns.countplot(x=x_data, hue=hue_data, data=my_data)
     ```

2. **[Themes](https://seaborn.pydata.org/tutorial/aesthetics.html#seaborn-figure-styles)**: Seaborn offers five preset themes: *darkgrid*, *whitegrid*, *dark*, *white*, and *ticks*. Each theme is designed to cater to different applications and personal preferences, with *darkgrid* being the default.

   - Example 1: The *darkgrid* theme provides a dark background with gridlines, enhancing clarity and serving as a helpful reference for quantitative comparisons.
     ```
     sns.set_style(style="darkgrid")
     sns.countplot(x=x_data, hue=hue_data, data=my_data)
     ```
     
   - Example 2: The *whitegrid* theme features a white background with gridlines, making it ideal for plots with dense data, as it improves readability.
     ```
     sns.set_style(style="whitegrid")
     sns.countplot(x=x_data, hue=hue_data, data=my_data)
     ```

   - Example 3: The *dark* theme offers a sleek look with a solid dark background, suitable for formal presentations.
     ```
     sns.set_style(style="dark")
     sns.countplot(x=x_data, hue=hue_data, data=my_data)
     ```

3. **Labels and Titles**: Clear labels and titles are essential for conveying the plot's message. This can be achieved by using Matplotlib's [plt.xlabel()](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlabel.html), [plt.ylabel()](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylabel.html), and [plt.title()](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html) functions. Ensure that axes are labeled appropriately and provide a descriptive title that summarizes the plot's content.
   - Example:
     ```
     plt.title('Data Insights Visualization')
     plt.xlabel('X-axis Label')
     plt.ylabel('Y-axis Label')
     ```

4. **[Legends](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html)**: Legends clarify the meaning of different colors or symbols in your plot. Proper positioning of the legend can reduce clutter and improve readability, with the option to move it outside the main plot area for enhanced clarity.
   - Example:
      ```
      plt.legend(title='Legend Title', bbox_to_anchor=(1.05, 1), loc='upper left')
      ```
    
   - **Additional Customizations**:
        - **Increase the size of the legend**: 
        Adjusting the font size of the legend ensures that its text is more prominent and easier to read, especially when dealing with detailed or complex plots.
            ```
             plt.legend(title='Legend Title', loc='center left', fontsize=12)
            ```    
     
        - **Remove the border around the legend**: 
        Eliminating the border around the legend creates a sleeker and cleaner design, allowing the focus to remain on the data visualization itself.
     
            ```>
             legend = plt.legend(title='Legend Title', loc='center left')
             legend.get_frame().set_edgecolor('none')
            ```

        - **Set the legend background color to white**:
        Changing the legend’s background to white improves its contrast against the plot, ensuring that the legend remains distinct and easy to read without overwhelming the plot.
             ```
             legend.get_frame().set_facecolor('white')
             ```

     <details> 
     <summary><strong>Detailed Parameters Explanation</strong></summary>
     <ul>
        <li><strong><code>loc</code> parameter</strong>: Controls where the legend appears on the plot, with options like <i> upper right </i>, <i> lower left </i>, or <i>center</i>. The <i>best</i> value selects the optimal position with minimal overlap.</li>
        <li><strong><code>bbox_to_anchor</code> parameter</strong>: Fine-tunes the legend's location outside the plot. The tuple <i>(1.05, 1)</i> positions the legend just outside the right edge of the plot area, with 1.05 indicating a slight offset to the right and 1 placing it vertically centered. The <i>x</i> value ranges from 0 (left edge) to 1 (right edge) of the axes, while the <i>y</i> value ranges from 0 (bottom edge) to 1 (top edge) of the axes.</li>
        <li><strong><code>fontsize</code></strong>: Adjusts the size of the legend text for improved readability.</li>
        <li><strong><code>get_frame()</code></strong>: Allows customization of the legend box, including setting the background (`set_facecolor()`) and border (`set_edgecolor()`).</li>
     </ul>
     </details>

5. **Font and Text Customization**:  Customizing fonts and text properties can improve the plot's readability and align with the theme of your project. Seaborn and Matplotlib provide various options for font customization.

   - Example: Customizing the font size and style.
     ```
     plt.title('Data Insights Visualization', fontsize=14, fontweight='bold')
     plt.xlabel('X-axis Label', fontsize=12)
     plt.ylabel('Y-axis Label', fontsize=12) 
     ```

   - Example: Changing the font family to a specific style.
     ```
     plt.rcParams['font.family'] = 'serif'
     ```
   
6. **Tight Layout**: Utilizing the `tight_layout()` function optimizes the spacing between subplots and plot elements, ensuring that labels and titles fit well within the figure area.
   - Example:
     ```
     plt.tight_layout()
     ```

### Task: Enhance the Visualization Design

#### Objective

The goal of this task is to apply advanced design techniques to the previously created count plot, improving its overall aesthetic and making the information more accessible.
<img src="../../common/resources/images/example.png" alt="">

#### Steps to Follow

1. **Set Color Palette**: 
   - Choose a darkrid color palette that suits your data's theme using Seaborn's palette functions.

2. **Customize the Legend**:
   - Move the legend outside of the plot area for better clarity and organization. 
   <div class="hint">
     Use tuple (1, 0.5) for <code>bbox_to_anchor</code> parameter.
   </div>
   <div class="hint">
     Use 'center left' position for location of the legend.
   </div>


3. **Utilize Tight Layout**: 
   - Improve the spacing of elements in the plot.

4. **Display the Enhanced Plot**: 
   - Finally, use `plt.show()` to render the updated visualization with the applied design improvements.

### Conclusion

By integrating these advanced design techniques, visualizations can be made not only more informative but also more visually appealing, aiding in the effective communication of data insights.
